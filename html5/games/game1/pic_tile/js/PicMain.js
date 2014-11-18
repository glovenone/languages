/**
 * Created with JetBrains WebStorm.
 * User: Predaking
 * Date: 13-10-24
 * Time: 下午1:49
 * To change this template use File | Settings | File Templates.
 */

init(40,"mytest",480,800,main);

/**层变量*/
//显示进度条所用层
var loadingLayer;
//游戏最底层
var backLayer;

var loadIndex = 0;
//图片path数组
var imgData = new Array();
//读取完的图片数组
var imglist = {};
var imgLength = 12;

var curIndex;
var buferIndex;
var gameLevel;

var state;
var bmpData;
var gameBmp;
var bmpBack;
//var bmpTiles;
//var bmpTileBack;

var teamTiles;
var gamePoint;


var backLayer;
var frameLayer = null;

var offsetX = 40;
var offsetY = 360;
var tileWH;

var txt;


function main(){
    LGlobal.setDebug(true);

    //准备读取图片
    for(var i = 0; i < imgLength; i++)
    {
        imgData.push({name:"pic"+i,path:"./images/img"+i+".png"});
    }
    imgData.push({type:"js",path:"./js/glb.js"});
    imgData.push({type:"js",path:"./js/ShowTile.js"});
    imgData.push({name:"back",path:"./images/bk.png"});



    loadingLayer = new LoadingSample1();
    addChild(loadingLayer); 
    LLoadManage.load(
        imgData,
        function(progress){
            loadingLayer.setProgress(progress);
        },
        function(result){
            imglist = result;
            removeChild(loadingLayer);
            loadingLayer = null;
            gameInit();
        }
    );
}


var ls1;
function gameInit(){
    backLayer = new LSprite();
    addChild(backLayer);
//    frameLayer = new LSprite();
//    addChild(frameLayer);

    bmpData = new Array();
    for(var i = 0; i < imgLength; i++)
    {
        bmpData.push(new LBitmapData(imglist["pic"+i]));
    }
    bmpBack = new LBitmap(new LBitmapData(imglist["back"]));


    gameLevel = 2;
//    newGame();
    setState(Global.STATE_RUN);

    //添加贞事件，开始游戏循环
    backLayer.addEventListener(LEvent.ENTER_FRAME,updateFrame);
    //添加控制事件
    backLayer.addEventListener(LMouseEvent.MOUSE_DOWN,ondown);
    backLayer.addEventListener(LMouseEvent.MOUSE_UP,onup);
    trace("5");
}



function newGame(){

    backLayer.removeAllChild();
    backLayer.addChild(bmpBack);
//    frameLayer.removeAllChild();

    if(frameLayer != null){
        removeChild(frameLayer);
    }
    frameLayer = new LSprite();
    addChild(frameLayer);


    gamePoint = gameLevel * gameLevel;

    var tempArys = new Array();
    for(var i = 0; i < imgLength; i++)
    {
        tempArys.push(i);
    }
    var ids = Global.getRandomArray(tempArys,4);
    gameBmp = new LBitmap(bmpData[ids[0]]);//第0个图为当前用的图
    var sprGameBmp = new LSprite();
    sprGameBmp.addChild(gameBmp);
    sprGameBmp.scaleX = 0.625;
    sprGameBmp.scaleY = 0.625;
    sprGameBmp.x = 160;
    sprGameBmp.y = 40;
    backLayer.addChild(sprGameBmp);

    teamTiles = new Array();
    //把用到的图块拆出来，放到2维数组bmpTiles里
    var x = 0;
    var y = 0;
    var len = Global.getInt(gameBmp.getWidth()/gameLevel);
//    trace("1");

    //框子信息
    tileWH = getSideSize();
//    touchRects = new Array();
    var xfrm = offsetX;
    var yfrm = offsetY;

//    trace("2");
    for(var i = 0; i < gameLevel; i++){
        for(var j = 0; j < gameLevel; j++){
            //tile
            var tileTeam = new ShowTile(getMaxWaitCount());
            for(var id = 0; id < ids.length; id++){
                var tempBmpData = new LBitmapData(imglist["pic"+ids[id]],x,y,len,len);
                var tempBmp = new LBitmap(tempBmpData);
                var tempSpr = new LSprite();
                tempSpr.addChild(tempBmp);
                tempSpr.scaleX = Global.TILE_ZOOM;
                tempSpr.scaleY = Global.TILE_ZOOM;
                tileTeam.addTile(tempSpr);
            }
            tileTeam.randomTiles();
            tileTeam.setRect(xfrm ,yfrm,tileWH,tileWH);
            teamTiles.push(tileTeam);
            backLayer.addChild(tileTeam);

            x += len;
            //框子
            frameLayer.graphics.drawRect(4,"#000000",[xfrm ,yfrm,tileWH,tileWH],false);
            frameLayer.graphics.drawRect(2,"#ffffff",[xfrm ,yfrm,tileWH,tileWH],false);
            xfrm += tileWH;
        }
        x = 0;
        y += len;
        xfrm = offsetX;
        yfrm += tileWH;
    }


//    trace("3");
    txt = new LTextField();
    txt.text = "请按照上面的图选择图块";
    txt.color = "#000000";
    txt.x = 10;
    txt.y = 300;
    txt.size = 16;
    frameLayer.addChild(txt);

//    trace("4");
//    setState(Global.STATE_RUN);
}

function setState(ste){
    state = ste;
    switch (state){
        case Global.STATE_RUN:
            newGame();
            break;
        case Global.STATE_END:
            endGame();
            break;
    }
}

function endGame(){
//    frameLayer.removeAllChild();
    txt.text = "恭喜过关，点击屏幕继续下一关";
    txt.color = "#ff0000";
    if(gameLevel < 4){
        gameLevel ++;
    }
}

function getMaxWaitCount(){
    return 25;
}

function getSideSize(){
    return Global.getInt(400/gameLevel);
}

function updateFrame(){
//    trace("5");
//    txt.text = "请按照上面的图选择图块" + gamePoint;
    switch (state){
        case Global.STATE_RUN:
            updateGame();
            break;
        case Global.STATE_END:
            updateGameEnd();
            break;
    }
}
function updateGameEnd(){
    if(isTouch){
        setState(Global.STATE_RUN);
        isTouch = false;
    }
}

function updateGame(){
    var point = 0;
    for(var i = 0; i < teamTiles.length; i++){
        teamTiles[i].update();
        if(isTouch){
            teamTiles[i].onClicked(LGlobal.offsetX,LGlobal.offsetY);
        }
        if(teamTiles[i].isRight){
            point++;
        }
    }
    isTouch = false;
    if(point == gamePoint){
        setState(Global.STATE_END);
    }
}

function onup(event){
    isTouch = false;
}
var isTouch = false;
function ondown(event){
    isTouch = true;
}

























