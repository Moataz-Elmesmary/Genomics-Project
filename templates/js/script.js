window.addEventListener('scroll', function(){
    const header = this.document.querySelector('header');
    header.classList.toggle ("sticky",window.scrollY > 0);
});




AOS.init();









var owl = $('.owl-carousel');
owl.owlCarousel({
    items:3,
    loop:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:1000,
    autoplayHoverPause:true
});
$('.play').on('click',function(){
    owl.trigger('play.owl.autoplay',[1000])
})
$('.stop').on('click',function(){
    owl.trigger('stop.owl.autoplay')
})

