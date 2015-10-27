window.onload = function() {
//    animateLogo();
    animateRobot();
}
function animateLogo() {
    TweenMax.fromTo("#react-logo",1.5, {
        // from
        css: {
                 // 使用 CSS3 transform
                 y: "-15px",
             }
    },{
        // to
        css: {
                 y: "15px",
             },

    // 永久重复动画的选项
    repeat: -1,

    // 反转、重新运行动画的选项
    yoyo: true,

    ease: Power2.easeInOut,
    });
}

function animateRobot() {
    var t = new TimelineMax({yoyo:true, repeat:-1, repeatDelay:0.5});
    box = "#android-robot";
    t.to( box,0.5, {
        rotation: "-=10deg",
    })
}
