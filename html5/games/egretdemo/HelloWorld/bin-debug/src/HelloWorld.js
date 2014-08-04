var __extends = this.__extends || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    __.prototype = b.prototype;
    d.prototype = new __();
};
var HelloWorld = (function (_super) {
    __extends(HelloWorld, _super);
    function HelloWorld() {
        _super.call(this);
        this.addEventListener(egret.Event.ADDED_TO_STAGE, this.onAddToStage, this);
    }
    HelloWorld.prototype.onAddToStage = function (event) {
        egret.Profiler.getInstance().run();
        var _myGrid = new GridSprite();

        this.addChild(_myGrid);
        console.log('Hello world!');
    };

    HelloWorld.prototype.sprTest = function () {
        var spr = new egret.Sprite();
        spr.x = 100;
        spr.y = 20;
        spr.scaleX = 0.5;
        spr.scaleY = 0.5;
        spr.alpha = 0.4;
        spr.rotation = 30;
    };
    return HelloWorld;
})(egret.DisplayObjectContainer);
