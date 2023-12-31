let slug = url => new URL(url).pathname.match(/[^\/]+/g)
let captcha = slug(window.location.href)
if (captcha && captcha.slice(-1)[0] == "invalid") {
    window.location.replace("#contact");
} 

/*Navigation drop*/
$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

/*Burger menu */
function menu(x) {
	x.classList.toggle('anim');
}

/*Slider first*/
$('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  draggable: false,
  touchMove: false,
  swipeToSlide: false,
  swipe: false,
  arrows: false,
  infinite: false
});

$('.slider-nav').slick({
  centerMode: true,
  slidesToShow: 4,
  slidesToScroll: 0,
  asNavFor: '.slider-for',
  vertical: true,
  dots: false,
  focusOnSelect: true,
  arrows: false,
  centerMode: true,
});


/*Slider second*/
$('.slider-description-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  infinite: true,
  focusOnSelect: true,
});
$('a[data-slide]').click(function(e) {
  e.preventDefault();
  var slideno = $(this).data('slide');
  $('.slider-description-for').slick('slickGoTo', slideno - 1);
});
