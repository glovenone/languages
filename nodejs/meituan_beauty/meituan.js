'use strict';
const city_url = require('./config/city_url');
let city = process.argv[2] || 'bj';
if (!city_url[city]) {
  console.warn('unknown city code');
  process.exit(0);
}
console.log('**start**' + new Date().toJSON());
const co = require('co');
const async = require('async');
const urllib = require('urllib');
const cheerio = require('cheerio');
const shop_model = require('./models/shop');

let shop = shop_model(city);
let url_detail_main = 'http://www.meituan.com/shop/';
let url_detail = city_url[city].detail;
let url_index = city_url[city].index;
let url_page = city_url[city].page;
let idArr = [];
let pageMax = 0;
let isMaxPage = 0;//TODO
let i = 1;
let _reqRecoder = {};

const saveDetail = (shopid, data, callback)=> {
  let $ = cheerio.load(data);
  let $bread_nav = $('.bread-nav');
  let $bread_nav_a = $bread_nav.find('a');//面包屑导航，包含了商圈信息
  let $num = $('.num');
  let area;
  if ($bread_nav_a.length) {
    area = $bread_nav_a.eq(0).text() + $bread_nav.eq(1).text() + $bread_nav.eq(2).text();
  } else {
    area = $bread_nav.text();
  }
  let info = {
    shopid: shopid,
    area: area,
    name: $('.title').eq(0).text(),
    addr: $('.geo').text(),
    num1: $num.eq(0).text(),//消费人数,
    num2: $num.eq(1).text(),//评价人数
    phone: $('.under-title').last().html(),
    level: $('.biz-level').last().find('strong').text()
  };
  shop.upsert(info).then(()=> callback(null)).catch(callback);
};

const getDetail = (id, callback, crossCity, again)=> {
  let url = crossCity ? url_detail_main : url_detail;
  urllib.request(url + id, {timeout: 30000, dataType: 'text'})
    .then(res=> {
      let data = res.data.toString('utf-8');
      if (data.length) {
        saveDetail(id, res.data, callback)
      } else if (!again) {
        getDetail(id, callback, 1, 1);
      }
    })
    .catch(err=> {
      console.warn(id + '：' + err.message);
      getDetail(id, callback);
    })
};

const getDetails = ids=> {
  async.mapLimit(ids, 60, (id, callback)=> {
    getDetail(id, callback);
  }, (err, res)=> {
    if (err) return console.error(err);
    console.log(new Date().getTime());
    console.log('**done**' + new Date().toJSON());
  })
};

const pageHandler = (data, i)=> {
  let $ = cheerio.load(data);
  let data_async_params = $('.J-scrollloader.cf.J-hub').attr('data-async-params');
  if (data_async_params) {
    let ids = JSON.parse(JSON.parse(data_async_params).data).poiidList;
    console.log(`**page：${i}，count：${ids.length}**`);
    Array.prototype.push.apply(idArr, ids);
  }
  if ($('.no-poilist').length) {
    isMaxPage = 1;
    pageMax = i - 1;
    console.log(`max page ${pageMax}`);
  }
};

const main = (timeout)=> {
  timeout = timeout || 500;
  co(function* () {
    while (!isMaxPage) {
      let url = i === 1 ? url_index : url_page + i;
      if (!_reqRecoder[i]) {
        let now = new Date;
        _reqRecoder[i] = now.getMinutes() + '：' + now.getSeconds();
        let res = yield urllib.request(url, {dataType: 'text', timeout: timeout});
        pageHandler(res.data, i);
      }
      i++;
    }
    console.log(`total：${idArr.length}`);
    getDetails(idArr);
  }).catch(err=> {
    console.warn(`${i}：${err.name}`);
    isMaxPage = 1;//stop loop
    isMaxPage = 0;
    console.log('restart');
    main(5000);
  })
};

main(200);