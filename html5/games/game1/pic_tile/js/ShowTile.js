/**
 * Created with JetBrains WebStorm.
 * User: Predaking
 * Date: 13-10-24
 * Time: 下午7:56
 * To change this template use File | Settings | File Templates.
 */

function ShowTile(countMax){
    base(this,LSprite,[]);
    var self = this;
    self.tileSprs = new Array();
    self.maxCount = countMax;
    self.maxActionCount = 10;
    self.curCount = Global.getRandomIn(countMax/4,countMax);
    self.state = ShowTile.STATE_WAIT;
    self.curIndex = 0;
    self.nextIndex = 0;
    self.rect = null;
    self.actionDirection = Global.getRandomIn(0,3);
    self.rightTile = null;
    self.colorFrame = new LSprite();
    self.isRight = false;
};
ShowTile.STATE_WAIT = 0;
ShowTile.STATE_ACTION = 1;
ShowTile.STATE_SELECTED = 2;

ShowTile.prototype.addTile = function(tile){
    var self = this;
    self.tileSprs.push(tile);
    self.addChild(tile);
    tile.visible = false;
    if(self.rightTile == null){
        self.rightTile = tile;
    }
}

ShowTile.prototype.randomTiles = function (){
    var self = this;
    self.tileSprs.sort(function () { return 0.5 - Math.random(); });
    self.tileSprs[self.curIndex].visible = true;
    self.addChild(self.colorFrame);
    self.colorFrame.visible = false;
}

ShowTile.prototype.setRect = function (x,y,w,h){
    var self = this;
    self.rect = new LRectangle(x,y,w,h);
    self.x = x;
    self.y = y;
}

ShowTile.prototype.update = function (){
    var self = this;

    switch (self.state){
        case ShowTile.STATE_WAIT:
            self.curCount--;
            if(self.curCount <= 0){
                self.setState(ShowTile.STATE_ACTION);
            }
            break;
        case ShowTile.STATE_ACTION:
            if(self.actionTile()){
                self.setState(ShowTile.STATE_WAIT);
            }
            break;
        case ShowTile.STATE_SELECTED:
            break;
    }
}

ShowTile.prototype.actionTile = function(){
    var self = this;
    self.curCount--;
    var tileCur = self.tileSprs[self.curIndex];
    var tileNext = self.tileSprs[self.nextIndex];
    var zoom = self.curCount/self.maxActionCount;




    switch (self.actionDirection){
        case 0://左
            tileCur.scaleX = Global.TILE_ZOOM * zoom;
            tileNext.scaleX = Global.TILE_ZOOM - tileCur.scaleX;
            tileNext.x = self.rect.width * zoom;
            tileCur.x = 0;
            break;
        case 1://右
            tileCur.scaleX = Global.TILE_ZOOM * zoom;
            tileNext.scaleX = Global.TILE_ZOOM - tileCur.scaleX;
            tileCur.x = self.rect.width * (1 - zoom);
            tileNext.x = 0;
            break;
        case 2://上
            tileCur.scaleY = Global.TILE_ZOOM * zoom;
            tileNext.scaleY = Global.TILE_ZOOM - tileCur.scaleY;
            tileNext.y = self.rect.width * zoom;
            tileCur.y = 0;
            break;
        case 3://下
            tileCur.scaleY = Global.TILE_ZOOM * zoom;
            tileNext.scaleY = Global.TILE_ZOOM - tileCur.scaleY;
            tileCur.y = self.rect.width * (1 - zoom);
            tileNext.y = 0;
            break;
    }
    if(!tileNext.visible){
        tileNext.visible = true;
    }
    if(self.curCount <= 0){
        tileCur.visible = false;
        self.curIndex = self.nextIndex;
        tileNext.scaleX = Global.TILE_ZOOM;
        tileNext.scaleY = Global.TILE_ZOOM;
        tileNext.x = 0;
        tileNext.y = 0;
        tileCur.scaleX = Global.TILE_ZOOM;
        tileCur.scaleY = Global.TILE_ZOOM;
        tileCur.x = 0;
        tileCur.y = 0;
        return true;
    }
    return false;
}


ShowTile.prototype.setState = function (ste){
    var self = this;
    self.state = ste;
    self.colorFrame.visible = false;
    switch (self.state){
        case ShowTile.STATE_WAIT:
            self.curCount = self.maxCount;

            break;
        case ShowTile.STATE_ACTION:
            self.curCount = self.maxActionCount;
            self.nextIndex = self.curIndex + 1;
            if(self.nextIndex >= self.tileSprs.length){
                self.nextIndex = 0;
            }
            self.actionDirection =  Global.getRandomIn(0,3);
            break;
        case ShowTile.STATE_SELECTED:

            self.colorFrame.visible = true;
            if(self.rightTile == self.tileSprs[self.curIndex])
            {
                self.colorFrame.graphics.drawRect(5,"#00ff00",[3,3,self.rect.width - 6,self.rect.height - 6],false);
                self.isRight = true;
            }
            else{
                self.colorFrame.graphics.drawRect(5,"#ff0000",[3,3,self.rect.width - 6,self.rect.height - 6],false);
                self.isRight = false;
            }
            break;
    }

}

ShowTile.prototype.onClicked = function (x,y){
    var self = this;
    var rect = this.rect;
    if(x > rect.left && x < rect.right && y > rect.top && y < rect.bottom){
        switch (self.state){
            case ShowTile.STATE_WAIT:
                self.setState(ShowTile.STATE_SELECTED);
                break;
            case ShowTile.STATE_ACTION:
                var tileCur = self.tileSprs[self.curIndex];
                var tileNext = self.tileSprs[self.nextIndex];
                if(self.curCount > self.maxActionCount/2){
                    tileNext.visible = false;
                }
                else{
                    self.curIndex = self.nextIndex;
                    tileCur.visible = false;
                }
                tileNext.scaleX = Global.TILE_ZOOM;
                tileNext.scaleY = Global.TILE_ZOOM;
                tileNext.x = 0;
                tileNext.y = 0;
                tileCur.scaleX = Global.TILE_ZOOM;
                tileCur.scaleY = Global.TILE_ZOOM;
                tileCur.x = 0;
                tileCur.y = 0;
                self.setState(ShowTile.STATE_SELECTED);
                break;
            case ShowTile.STATE_SELECTED:
                self.setState(ShowTile.STATE_ACTION);
                break;
        }
    }

}