$(document).ready(function () {
    // ------------------------------------------ Navigation Bar ------------------------------------------ //
    window.addEventListener('DOMContentLoaded', function () {
        $(window).onload(function () {
            $('.navbar').css({
                height: "100px",
                'background-image': "linear-gradient(300deg, #ff7700,#ffa74d,#ffd89f)",
            });
        });
    });

    window.addEventListener('scroll', function() {
        if (window.scrollY >= 10) {
            $(window).scroll(function() {
                $('.navbar').css({
                    'background-image': "linear-gradient(rgba(0,0,0,0))",
                    transition: "1s",
                    height: "60px",
                });
            });
        }
    });

    // ------------------------------------------ Brand Examples ------------------------------------------ //
    const images = [{
            id: 0,
            name: "Samsung Galaxy S10E",
            image: "./static/images/samsungS10E.jpg",
        },
        {
            id: 1,
            name: "iPhone 11",
            image: "./static/images/iphone.png",
        },
        {
            id: 2,
            name: "Huawai P30 Pro",
            image: "./static/images/HuaweiP30.jpg",

        },
    ]

    images.forEach(bName => {
        $('.brand-example-names-home').append("<div class='brandName'>" + bName.name + "</div>");
        $('.brandName').mouseenter(function () {
            let index = $('.brandName').index(this);
            if (index == bName.id) {
                $('.brand-img').removeClass('initial-brand-img').css({
                    backgroundImage: "url('" + bName.image + "')",
                });
                $(this).css({
                    color: "skyblue",
                    textDecoration: "underline"
                });
            }
        });
        $('.brandName').mouseout(function () {
            let index = $('.brandName').index(this);
            if (index == bName.id) {
                $(this).css({
                    color: "black",
                    textDecoration: "none"
                });
            }
        })
    });
});