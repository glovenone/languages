class HelloWorld extends egret.DisplayObjectContainer {
    public constructor() {
        super();
        this.addEventListener(egret.Event.ADDED_TO_STAGE, this.onAddToStage, this);
    }

    private onAddToStage(event:egret.Event) {
        egret.Profiler.getInstance().run();
        var _myGrid:GridSprite = new GridSprite();

        this.addChild(_myGrid);
        console.log('Hello world!');
    }

    private sprTest() {
        var spr:egret.Sprite = new egret.Sprite()
        spr.x = 100;
        spr.y = 20;
        spr.scaleX = 0.5;
        spr.scaleY = 0.5;
        spr.alpha = 0.4;
        spr.rotation = 30;
    }


}