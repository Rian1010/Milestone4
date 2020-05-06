$(document).ready(function () {
    // ------------------------------------------ Navigation Bar ------------------------------------------ //

    let scroll_pos = 0;
    $(document).scroll(function () {
        scroll_pos = $(this).scrollTop();
        if (scroll_pos < 100) {
            $(".navbar").addClass('orange').removeClass('transparent').css({
                transition: "1s",
                height: "100px",
            });
        } else if (scroll_pos >= 100) {
            $('.navbar').addClass('transparent').removeClass('orange').css({
                transition: "1s",
                height: "60px",
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
            name: "Huawei P30 Pro",
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

    // ------------------------------------------ Smartphone Photography Examples ------------------------------------------ //

    for (let i = 0; i < 3; i++) {
        $('#smartphonePhotography${[i]}').mouseenter(function () {
            $('#smartphonePhotography${[i]}').children().slideDown(500);
        });
        $('#smartphonePhotography${[i]}').mouseout(function () {
            $('#smartphonePhotography${[i]}').children().slideUp(500);
        });
    }
});