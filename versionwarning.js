(function() {
    const regex = /archive\/\d\.\d+/;
    
    var showWarning = (msg) => {
        $('.content').prepend(
            '<br>' +
            '<p style="' +
            [
                'margin-top: 1px',
                'padding: 1em',
                'font-size: 1.2em',
                'background: #ffeeee',
            ].join('; ') +
            '">' +
            '<a href="https://seaborn.pydata.org/" style="color: #333">' +
            'This is documentation for an old version. ' +
            'Click here to load docs for the latest release.' +
            '</a>' +
            '</p>')
    };
    var versionPath = location.pathname.split('/')[1];
    if (versionPath.match(regex)) { showWarning() }
})()

