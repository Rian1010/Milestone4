$(document).ready(function () {
    // ------------------------------------------ Navigation Bar ------------------------------------------ //
    $(window).on('load', function () {
        let scroll_pos = 0;
        $(document).scroll(function () {
            scroll_pos = $(this).scrollTop();
            if (scroll_pos < 100) {
                $(".navbar").addClass("blue").removeClass('see-through-blue-nav').css({
                    transition: ".5s",
                });
                $('.nav-link').css({
                    color: "#fff",
                });
            } else if (scroll_pos >= 100) {
                $('.navbar').addClass('see-through-blue-nav').removeClass("blue").css({
                    transition: "1s",
                });
                $('.nav-link').css({
                    color: "rgb(255, 188, 65)",
                });
            }
        });
    })

    // ------------------------------------------ Brand Examples ------------------------------------------ //
    const images = [{
            id: 0,
            name: "Samsung Galaxy S10E",
            image: "https://django-ecommerce-rian.s3.eu-central-1.amazonaws.com/static/images/samsungS10E.jpg",
        },
        {
            id: 1,
            name: "iPhone 11",
            image: "https://django-ecommerce-rian.s3.eu-central-1.amazonaws.com/static/images/iphone.png",
        },
        {
            id: 2,
            name: "Huawei P30 Pro",
            image: "https://django-ecommerce-rian.s3.eu-central-1.amazonaws.com/static/images/HuaweiP30.jpg",
        },
        {
            id: 3,
            name: "LG V30",
            image: "https://django-ecommerce-rian.s3.eu-central-1.amazonaws.com/static/images/LG-V30.jpg",
        },
        {
            id: 4,
            name: "Xiaomi Redmi Note 9 Pro-Max",
            image: "https://django-ecommerce-rian.s3.eu-central-1.amazonaws.com/static/images/xiaomi.jpg",
        },
    ]

    images.forEach(bName => {
        const brandNameClass = "<span class='brandName'>";
        $('.brand-example-names-home').append(`${brandNameClass + bName.name}</span>`);
        $('.brandName').mouseenter(function () {
            let index = $('.brandName').index(this);
            if (index == bName.id) {
                $('.brand-img').removeClass('initial-brand-img').css({
                    backgroundImage: "url('" + bName.image + "')",
                });
                $(this).css({
                    color: "skyblue",
                });
            }
        });
        $('.brandName').mouseout(function () {
            let index = $('.brandName').index(this);
            if (index == bName.id) {
                $(this).css({
                    color: "black",
                });
            }
        })
    });

    // ------------------------------------------ Login Username ------------------------------------------ //
    // Used the the following source for the code below: https://api.jquery.com/val/
    $("input[name = 'username']").keyup(function () {
        let nameVal = $(this).val();
        $('.username').text(` ${[nameVal]}`);
    });

    // ------------------------------------------  Ad Scroll Effect ------------------------------------------ //
    const intro = document.querySelector('.apple-ad-1');
    const video = document.getElementById('Ad1');

    // SCROLLMAGIC
    const controller = new ScrollMagic.Controller();

    // SCENES
    const scene = new ScrollMagic.Scene({
        duration: 30000,
        triggerElement: intro,
        triggerHook: 0
    })
    .addIndicators()
    .setPin(intro)
    .addTo(controller)

    // Video Animation
    let accelamount = 0.1;
    let scrollpos = 0;
    let delay = 0;

    scene.on('update', e => {
        scrollpos = e.scrollPos / 1000;
        console.log(e);
    });

    setInterval(() => {
        delay += (scrollpos - delay) * accelamount;
        console.log(scrollpos, delay);

        video.currentTime = delay
    }, 333.33);

});