'use strict';

const urllib = require('urllib');
const cheerio = require('cheerio');
let url_detail_main = 'http://www.meituan.com/shop/';
let url_detail = 'http://sz.meituan.com/shop/';
const getDetail = (id, callback, crossCity, again)=> {
  let url = crossCity ? url_detail_main : url_detail;
  urllib.request(url + id, {timeout: 30000, dataType: 'text'})
    .then(res=> {
      let data = res.data.toString('utf-8');
      if (data.length) {
        console.log('get data');
      } else if (!again) {
        console.log('need to get cross data');
        getDetail(id, callback, 1, 1);
      }
    })
    .catch(err=> {
      console.warn(id + '：' + err.message);
      getDetail(id, callback);
    })
};

getDetail(42343035, (err, data)=> {

});

//urllib.request(`http://sz.meituan.com/shop/42343035`, (err, data)=> {
//console.log(data.toString('utf-8').length);
//let $ = cheerio.load(data);
//let $bread_nav = $('.bread-nav').find('a');//面包屑导航，包含了商圈信息
//let area = $bread_nav.eq(0).text() + $bread_nav.eq(1).text() + $bread_nav.eq(2).text();
//let name = $('.title').eq(0).text();
//let addr = $('.geo').text();
//let phone = $('.under-title').last().html();
//let level = $('.biz-level').last().find('strong').text();//评分
//let $num = $('.num');
//let num1 = $num.eq(0).text();//消费人数
//let num2 = $num.eq(1).text();//评价人数
//let info = {
//  area: area,
//  name: name,
//  addr: addr,
//  phone: phone,
//  level: level,
//  num1: num1,
//  num2: num2
//};
//});