$('.owl-carousel').owlCarousel({
    rtl: true,
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
    }
})
window.addEventListener('scroll', function(){
    const header = this.document.querySelector('header');
    header.classList.toggle ("sticky",window.scrollY > 0);
});

AOS.init();
