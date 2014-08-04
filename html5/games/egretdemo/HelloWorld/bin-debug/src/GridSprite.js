var __extends = this.__extends || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    __.prototype = b.prototype;
    d.prototype = new __();
};
var GridSprite = (function (_super) {
    __extends(GridSprite, _super);
    function GridSprite() {
        _super.call(this);
        this.drawGrid();
    }
    GridSprite.prototype.drawGrid = function () {
        this.graphics.beginFill(0x0000ff);
        this.graphics.drawRect(0, 0, 50, 50);
        this.graphics.drawRect(50, 50, 50, 50);
        this.graphics.beginFill(0xff0000);
        this.graphics.drawRect(50, 0, 50, 50);
        this.graphics.drawRect(0, 50, 50, 50);
        this.graphics.endFill();
    };
    return GridSprite;
})(egret.Sprite);
