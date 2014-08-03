/**
 * Copyright (c) 2014,Egret-Labs.org
 * All rights reserved.
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Egret-Labs.org nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY EGRET-LABS.ORG AND CONTRIBUTORS "AS IS" AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL EGRET-LABS.ORG AND CONTRIBUTORS BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


declare module egret_native {

    /**
     * 游戏启动
     * @private
     */
    function startGame():void;

    /**
     * 启动主循环
     * @param callback 主循环回调函数
     * @param thisObject
     */
    function executeMainLoop(callback:Function, thisObject:any):void;


    function readXML(filepath:string):any;

    function readFileSync(filepath:string):any;


    function requireHttpSync(url:string,callback:Function):void;


    module Graphics {


        function clearScreen(r:number, g:number, b:number):void;

        function drawImage(texture:any, sourceX, sourceY, sourceWidth, sourceHeight, destX, destY, destWidth, destHeight):void;

        function setTransform(a:number, b:number, c:number, d:number, tx:number, ty:number):void;

        function setGlobalAlpha(alpha:number):void;

        function pushRectStencil(x:number,y:number,w:number,h:number,r:number,g:number,b:number,a:number,hackFlag:number,forceCreateMask:boolean):void;

        function popStencil():void;

    }

    module Label {

        function createLabel(font:string, size:number, defaultString:string):void;

        function setTextColor(color:number):void;

        function drawText(text:string, x:number, y:number):void;

        function setTextAlignment(type:string):void;

        function getTextSize(text:string):Array<number>;


    }


    module EGTXML {


        function readXML(filepath:string):void;
    }

    module Texture {

        function addTexture(filePath:string):any;

        function removeTexture(filePath:string):void;
    }
}