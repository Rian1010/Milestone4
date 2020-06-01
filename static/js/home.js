$(document).ready(function () {
    // ------------------------------------------ Navigation Bar ------------------------------------------ //
    $(window).on('load', function () {
        let scroll_pos = 0;
        $(document).scroll(function () {
            scroll_pos = $(this).scrollTop();
            if (scroll_pos < 100) {
                $(".navbar").addClass("blue").removeClass('see-through-blue').css({
                    transition: ".5s",
                });
                $('.nav-items-background').addClass("blue").removeClass('see-through-blue').css({
                    transition: ".5s",
                });
                $('.nav-link').css({
                    color: "#fff",
                });
            } else if (scroll_pos >= 100) {
                $('.navbar').addClass('see-through-blue').removeClass("blue").css({
                    transition: "1s",
                });
                $('.nav-items-background').addClass('see-through-blue').removeClass("blue").css({
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

    $("input[name = 'username']").keyup(function () {
        let nameVal = $(this).val();
        $('.username').text(` ${[nameVal]}`);
    });
});