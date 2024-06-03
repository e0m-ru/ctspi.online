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

// search
document.getElementById("searchInput").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        e.preventDefault();
        document.getElementById("searchForm").submit();
    }
});

// menu
var link = document.querySelector('#menu_trigger');
var elem = document.querySelector('#menu');

link.addEventListener('click', function () {
    elem.classList.toggle('show')
    link.classList.toggle('show')
});