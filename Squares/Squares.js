$(document).ready(function(){
    clicked = [];
    
    $('.box').one('click', registerClick)
    
    function registerClick(event){
        handleClick(event.target);
        
        if (clicked.length >= 7) {
            animateOffBoxes();
        }
    }
    
    function handleClick(target){
        var $box = $(target);
        $box.addClass('clicked');
        clicked.push($box);
    }
    
    function animateOffBoxes(){
        var $glint = $('.glint');
        $glint.toggleClass('in-progress');
        
        var intervalID = setInterval(function(){
            var $box = clicked.pop();
            $box.removeClass("clicked");
            if (clicked.length <= 0) {
                handleAnimEnd(intervalID)
            }
        }, 1000)
    }
    
    function handleAnimEnd(intervalID){
        clearInterval(intervalID);
        $('.box').one('click', registerClick);
        
        $('.glint').toggleClass('in-progress');
    }
})