
window.addEventListener('scroll', function(){
    const header = this.document.querySelector('header');
    header.classList.toggle ("sticky",window.scrollY > 0);
});
AOS.init();
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:40,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})