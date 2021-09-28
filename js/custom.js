function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

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

//     <button style="padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; border: 1px solid;" onclick="getPDF()">PDF</button>

// <button style="padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; border: 1px solid;" onclick="getRawmd()">Raw markdown</button>

function exists_p(ext) {
    var fn = window.location.href.replace('html', ext);
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', fn, false);
    xhr.send();
    return xhr.status !== 404;
}

function get_ext(ext) {
    var fn = window.location.href.replace('html', ext);
    window.open(fn);
}

function add_button(ext) {
    document.getElementById("versions").innerHTML += '\n' + '<button style="padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; border: 1px solid;" onclick="get_ext(' + ext + ')">' + ext + '</button>';
}

function add_if_exists(ext) {
    if(exists_p(ext)) {
	add_button(ext);
    }
}

function fill_versions() {
    add_if_exists('docx');
    add_if_exists('md');
    add_if_exists('pdf');
    add_if_exists('py');
}

fill_versions();
