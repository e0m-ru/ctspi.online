window.addEventListener('scroll', function () {
        var shrinkHeader = 1;
        // var header = document.querySelector('.header');
        var logo = document.querySelector('#logo');
        var scroll = window.pageYOffset || document.documentElement.scrollTop;

        if (scroll >= shrinkHeader) {
            // header.classList.add('shrink');
            logo.classList.toggle('big');
        } else {
            // header.classList.remove('shrink');
            logo.classList.toggle('big');
        }
    });