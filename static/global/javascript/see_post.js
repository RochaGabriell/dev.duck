var markdown = document.getElementById("markdown").value;
var converter = new showdown.Converter();
var html = converter.makeHtml(markdown);
document.getElementById("html").innerHTML = html;
document.getElementById("markdown").remove();