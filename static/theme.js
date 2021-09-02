function setTheme(themeCss, highlightThemeCss) {
    // set theme
    themeElement = document.getElementById("theme");
    themeElement.href = themeCss;

    // set highlight theme
    highlightThemeElement = document.getElementById("highlight-theme");
    highlightThemeElement.href = highlightThemeCss;
}

function setFont(fontCss) {
    // set font
    fontElement = document.getElementById("font");
    fontElement.href = fontCss;
}

function getPDF() {
    var pdf = window.location.href.replace('html', 'pdf');
    window.open(pdf);
}

function getRawmd() {
    var rawmd = window.location.href.replace('html', 'md');
    window.open(rawmd);
}
