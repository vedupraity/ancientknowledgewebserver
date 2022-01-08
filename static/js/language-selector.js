window.redirectTo = (url) => {
    window.location.href = url;
};

window.languageSelector = async () => {
    const { value: language } = await Swal.fire({
        template: '#language-selector-swal-template'
    });

    if (language) {
        if (window.location.pathname === '/') {
            window.redirectTo(`/${language}/`);
        } else {
            let currentPath = window.location.pathname;
            let newPath = currentPath.replace(/^\/[a-z]{2}\/?/, `/${language}/`);
            window.redirectTo(newPath);
        };
    } else {
        $('html').css('overflow-y', 'auto');
    };
};