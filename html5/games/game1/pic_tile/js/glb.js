/**
 * Created with JetBrains WebStorm.
 * User: Predaking
 * Date: 13-10-24
 * Time: 下午1:55
 * To change this template use File | Settings | File Templates.
 */

var Global = function (){throw "LEvent cannot be instantiated";};
Global.STATE_RUN = 0;
Global.STATE_END = 1;
Global.getRandomIn = function(a,b){
    return Math.floor(Math.random()*(b+1-a) + a);
};
Global.TILE_ZOOM = 400/256;

Global.getRandomArray = function(srcArys,getCount){
    var ids = new Array();
    var tempArys = new Array();
    for(var i = 0; i < imgLength; i++)
    {
        tempArys.push(srcArys[i]);
    }
    for(var i = 0; i < getCount; i++){
        var id = Global.getRandomIn(0,tempArys.length-1);
        ids.push(tempArys[id]);
        tempArys.splice(id,1);
    }
    tempArys = null;
    return ids;
};

Global.cloneObj = function(myObj){
    if(typeof(myObj) != 'object') return myObj;
    if(myObj == null) return myObj;

    var myNewObj = new Object();

    for(var i in myObj)
        myNewObj[i] = Global.cloneObj(myObj[i]);

    return myNewObj;
};

Global.getInt = function(value){
    return Math.floor(value);
};
