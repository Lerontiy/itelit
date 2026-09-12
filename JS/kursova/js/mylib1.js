$(function(){
	
//alert($('h1').text());

//1
$('#dialog').hide();

//2
$('#accordion').accordion({
	collapsible: true,
	active: false
});

//3
$('#drugainfa').hover(function(){
//4
	$('#drugainfa').css('color', '#303030');
},
function(){
	$('#drugainfa').css('color', '#303030');
});
//це треба було зробити, тому що без цього #drugainfa ставало погано
//можете самі перевірити

//5
$('#drugainfa').click(function(){
//6
	$('#dialog').dialog();
});

$('#elpochta').hover(function(){
//7
	$('#elpochta').text(':)');
},
	function(){
	$('#elpochta').text('qwerty@gmail.com');
});

var fontStateP = 0;
var fontStateM = 0;
$('.btn-fs').click(function(){
//ppppp
	var fontSize = parseInt($("body").css("font-size"));
//8
	if($(this).hasClass("plus-font-size"))
	{
		fontSize = fontSize + 1 + "px";		$("body").css({"font-size":fontSize});
		fontStateP++;
	}
	if($(this).hasClass("minus-font-size"))
	{
		fontSize = fontSize - 1 + "px";
		$("body").css({"font-size":fontSize});
		fontStateM++;
	}
	if($(this).hasClass("normal-font-size"))
	{
		if(fontStateP>0){
			fontSize = fontSize - fontStateP + "px";
			fontStateP = 0;
			$("body").css({"font-size":fontSize});
		}if(fontStateM>0){
			fontSize = fontSize + fontStateM + "px";
			fontStateM = 0;
			$("body").css({"font-size":fontSize});
		}
	}
});
//9
$('#zagolovok').dblclick(function(){
//10
	$("#zagolovok").animate({
		opacity: 0.4
	})
});


$("#content>h2").mouseenter(function(){
	$("#content>h2").css("color", "red")
});

$("#content>h2").mouseleave(function(){
	$("#content>h2").css("color", "#303030")
});



$("#sidebar>h2").hover(
function(){
	$("#sidebar>h2").css("color", "red")
},
function(){
	$("#sidebar>h2").css("color", "#303030")
});


//#303030






















});