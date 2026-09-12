$(function()
{
//t1
//z1
//alert($('h1').text());
//z2
//alert($('.link-moto').text());
//z3
//$(".slide-btn").hide(10000);
//$(".slide-btn").show(10000);
//z4
//$(".features-grid p").hide(3000);
//z5
//$(".categorie").show(2000);
//z6
//alert($('ul.top-nav>li').text());
//z7
//$(".slide-text>h1+span").hide(3500);
//$(".slide-text>h1+span").show(2000);
//z8
//$("h3>span").hide(1000);
//$("h3>span").show(2000);
//z9
//alert($('.blog-post-info>span>a').text());
//z10
//alert($('.blog-post-date>span>label').text());
//z11
//alert($('.blog-post-info>span+h4').text());
//z12
//$('img[src*=logo]').hide(3000);
//z13
//shovaty('my_form');
//shovaty('img_2');
//shovaty('moto_models');
//функція сховати
//function shovaty(name_id_obj)
//{
//	obj = $("#"+name_id_obj)
//	obj.hide(5000)
//}




//t2
//z1
//$(".slide-text>h1").fadeOut(3000);
//$(".slide-text>h1").fadeIn(3000);
//z2
//$(".head-moto-img").fadeTo("slow",0.05);
//$(".head-moto-img").fadeTo(7000,1);
//z3
//$(".head").slideUp(2000);	
//$(".head").slideDown(1000);
//z4
//$(".blog-post").fadeOut(1500);
//$(".blog-time-line").slideUp(2000);
//$(".blog-time-line").slideDown(3000);
//$(".blog-post").fadeIn(6000);
//z5
//zr(".head",3000,2000);
//function zr(name_obj,t1,t2)
//{
//	obj = $(name_obj);
//	t1 = t1;
//	t2 = t2;
//	obj.slideUp(t1);
//	obj.slideDown(t2);
//}
//z6
//prozor(".head",3000,0.2);
//prozor("#bigform",3000,0.5);
//function prozor(name_obj, time, opacity)
//{
//	obj = $(name_obj);
//	time=time;
//	opacity=opacity;
//	obj.fadeTo(time,opacity);
//	obj.slideUp(time);
//	obj.slideDown(time);
//	obj.fadeTo(time,1);
//}
//z7
//$(".top-nav>ul").hide(5000, function()
//{
//	alert("Меню було сховано");
//})
//z8
//$(".slide-text").slideUp(2000, function()
//{
//	zr(".head",3000,2000);
//	prozor("#bigform",3000,0.2);
//})




//t3
//z1
//$(".slide-btn").click(function()
//{
//alert("Була натиснута кнопка з класом slide-btn");
//});
//z2
//$('.features-grids').click(function()
//{
//	$('.head-moto-img').slideUp(3000);
//});
//z3
//$('.features-grids').click(function()
//{
//	$('.head-moto-img').slideToggle(500);
//});
//z4
//$('.head-moto-img').click(function()
//{
//	$(this).fadeToggle(2000);
//});
//z5
//$('.header').mouseenter(function()
//{
//	$('.slide-text').slideUp();
//});
//$('.header').mouseout(function()
//{
//	$('.slide-text').slideDown();
//});
//z6
$('.slide-btn').click(function()
{
	$(this).text('Оберіть мотоцикл нище на сторінці');
		
});
//z7
//$('#p').click(function()
//{
//	$('.head-moto-img').slideUp();
//});
//z8
//var text1 = "Подивитися фото";
//var text2 = "Сховати фото";
//
//$('#p').click(function()
//{
//	$('.head-moto-img').slideToggle();
//	if($('#p').text()!=text1)
//		$('#p').text(text1);
//	else
//		$('#p').text(text2);
//});
//z9
//$('.blog-post-date').hover(
//function()
//{
//	$('+.blog-post-info>.categorie',this).fadeIn();
//},
//function()
//{
//	$('+.blog-post-info>.categorie',this).fadeOut();
//}
//); 

//z10
//$('.contatct-active').click(
//function()
//{
//	if($('.m6>a').text()=="eng")
//	{
//		$('.m1>a').text('Home');
//		$('.m2>a').text('Motorcycles');
//		$('.m3>a').text('Sale');
///		$('.m4>a').text('Forum');
//		$('.m5>a').text('Contacts');
//		$('.m6>a').text('ua');
//	}
//	else
//	{
//		$('.m1>a').text('Головна');
//		$('.m2>a').text('Мотоцикли');
//		$('.m3>a').text('Розпродаж');
///		$('.m4>a').text('Форум');
//		$('.m5>a').text('Контакти');
//		$('.m6>a').text('eng');
//	}
//});




//t4
//$('p').click(function(){
//   $(this).text(function(i, origText){
//       return "Ви обрали: " + origText;
//   });
//})
//z1
//передає html код елемента
//$('li').click(function(){
//	alert($(this).html());
//});
//z2
//передає вміст комірки
//alert($('#email').val());
//z3
//передає значення атрибуту елемента
//$('.link-moto').click(function(){
//	alert($(this).attr('href'));
//});
//z4
//передає значення атрибуту елемента
//$('.head-moto-img').click(function(){
//	alert($(this).attr('src'));
//});
//z5
//передає html код елемента
//$('#p').click(function(){
//	$(this).html("<i><font color='grey'>Зараз функція //недоступна,<br> спробуйте пізніше</font></i>");
//});
//z6 
//$('.slide-btn').click(function(){
//	$('.m6').html("<img src='images/pic_eng.png' //width='50px'></img>");
//});
//z7
//$('.head-moto-img').click(function(){
//   $('+h3>a', this).text(function(i, origText){
//       return "Ви обрали: " + origText;
//  });
//});
//z8
//$('.head-moto-img').click(function(){
//   $('+h3>a', this).html(function(i, origText){
//       return "<i>Ви обрали:<i><br><br> " + origText;
//   });
//});
//z9
//var count = 0;
//$('.blog-post-date').hover(function(){
//$('+.blog-post-info>.categorie', this).text(function(i, //origText){
//	if(count==0){
//		count=1;
//		return "Бажаєте замовити? " + origText;
//	}
//});
///$('+.blog-post-info>.categorie', this).fadeIn();
//},
//function(){
//	$('+.blog-post-info>.categorie', this).fadeOut();
//});	
//z10	
//$('.blog-post-date').click(function(){
//	var obj = this;
//	$('#mytextarea').text(function(i, origText){
//		return origText + $('+.blog-post-info>h4',obj).text()+" "+$('+.blog-post-info>.categorie',obj).text()+ "\n";
//	});
//});
	
	
	

//t5	
//z1
//$("#about-moto").addClass("new");
//z2
//$("#about-moto").prepend("<p class='fon_yellow'>Цей абзац доданий за допомогою методу prepend1</p>");
//$("#about-moto").append("<p class='fon_yellow'>Цей абзац доданий за допомогою методу append2</p>");
//$("#about-moto").before("<p class='fon_yellow'>Цей абзац доданий за допомогою методу before3</p>");
//$("#about-moto").after("<p class='fon_yellow'>Цей абзац доданий за допомогою методу after4</p>");
//z3
//$("li").hover(
//	function(){
//		$(this).toggleClass("svitlo");
//	}
//);
//z4
//$('.head-moto-img').click(function(){
//	$(this).clone().prependTo(".koshik-wrapper");
//	$(".koshik-wrapper").addClass("full-koshik");
//});
//z5
//$('.head-moto-img').click(function(){
//	$(this).clone().appendTo(".koshik-wrapper");
//	$(this).remove();
//	$(".koshik-wrapper").addClass("full-koshik");
//});
//z6
//$('.head-moto-img').click(function(){
//	var n= $(this);
//	$('.koshik-wrapper-items').each(
//		function(){
//			if(n.attr('nomer')== $(this).attr('nomer')){
//				$(this).html(n.clone())
//				n.remove();
//				$(".koshik-wrapper").addClass("full-koshik");
//			}
//		}
//	)	
//});
//z7
//$('.head-moto-img').click(function(){
//	$('.koshik-wrapper').append($(this).clone().dblclick(function(){
//		$(this).remove();
//		Vsiogo();
//	}));
//	Vsiogo();
//});
//
//function Vsiogo(){
//	var count = 0;
//	var suma = 0;
//	
//	$(".koshik-wrapper>.head-moto-img").each(
//		function(){
//			count++;
//			suma+=parseInt($(this).attr('price'));
//		}
//	);
//$(".suma").html("Всього  <b> "+count+" </b>  мотоциклів на суму <b> "+suma+" </b> UAN");
//if(count>0){
//	$(".koshik-wrapper").addClass("full-koshik");
//}
//else{
//	$(".koshik-wrapper").removeClass("full-koshik");
//}
//}




//t6
//z1
//$('.slide-btn').height(100);
//z2
//change_width('.work-head>h3', 700);
//function change_width(selectorObj ,w)
//{
//	$(selectorObj).width(w);
//}
//z3
//change_width('.head-moto-img', 100);
//function change_width(selectorObj ,w)
//{
//	var oldW = $(selectorObj).width();
//	var rizn = w - oldW;
//	$(selectorObj).width(w).height($(selectorObj).height()+rizn)
//}
//z4
//$('.head-moto-img').click(function()
//{
//	change_width(this);
//});
//function change_width(selectorObj)
//{
//	var width = $(selectorObj).width();
//	var height = $(selectorObj).height();	
//	$(selectorObj).width(width/2).height(height/2);
//}
//z5
//$('.head-moto-img').click(function()
//{
//	var title = $(this).attr('title');
//	var width = $(this).width();
//	var height = $(this).height();
//	
//	if(title=="")
//	{
//		$(this).width(width/1.5).height(height/1.5);
//		$(this).attr("title", "1");
//	}
//	else
//	{
//		$(this).width(width*1.5).height(height*1.5);
//		$(this).attr("title", "");
//	}
//});
//z6
//$('.head-moto-img').hover(
//	function()
//	{
//		var width = $(this).width();
//		var height = $(this).height();
//		$(this).width(width/2).height(height/2);
//	},
//	function()
//	{
//		var width = $(this).width();
//		var height = $(this).height();
//		$(this).width(width*2).height(height*2);
//	});
//z7
//$('img').hover(
//		function()
//		{
//			change_width_s(this);
//		},
//		function()
//		{
//			change_width_b(this);
//		}
//	);
//	function change_width_b(selectorObj)
//	{
//		var width = $(selectorObj).width();
//		var height = $(selectorObj).height();
//		$(selectorObj).width(width*1.5).height(height*1.5);
//	}
//	function change_width_s(selectorObj)
//	{
//		var width = $(selectorObj).width();
//		var height = $(selectorObj).height();
//		$(selectorObj).width(width/1.5).height(height/1.5);
//	}
//z8
//$('.head-moto-img').hover(
//	function()
//	{
//		size_obj(this);
//	},
//	function()
//	{
//		$("#p").text("Сховати фото");
//	}
//);
//function size_obj(selectorObj)
//{
//	var alt = $(selectorObj).attr('alt');
//	var width = $(selectorObj).width();
//	var height = $(selectorObj).height();
//   
//$("#p").text("Об'єкт - Мотоцикл "+alt+". Його ширина = "+width+"px, висота = "+height+"px")
//}
//z9
//$('.head-moto-img').click(
//	function()
//	{
//		getInfoImg(this);
//	}
//);
//function getInfoImg(selectorObj)
//{
//	var src = $(selectorObj).attr('src');
//	var width = $(selectorObj).width();
//	var height = $(selectorObj).height();  
//$(".koshik-wrapper").append("Об'єкт - Мотоцикл "+src+". Його ширина = "+width+"px, висота = "+height+"px<br>");
//}




//t7
//z1
//$(':header').first().css("background-color", "yellow");
//z2
//$(':header').last().css("font-size", "400%");
//z3
//$("input[type='checkbox']").eq(1).prop('checked', true);
//z4
//$("input[type='radio']").first().prop('checked', true);
//z5
//$('#my_form').click(function()
//{
//	getInfoMoto();
//});
//function getInfoMoto()
//{
//	var moto = $('#motoSelect option:selected').text();
//	var days = $('#daysSelect option:selected').text();
//	var email = $('#email').val();
//	var shlem = "";
//	var bag = "";
//	var od = "";
//	var inch = "";
//	
//	if($("input[type='checkbox']").eq(0).prop('checked')==true)
//	{
//		shlem = $("label[for='shlem']").text();
//	}
//	if($("input[type='checkbox']").eq(1).prop('checked')==true)
//	{
//		bag = $("label[for='bag']").text();
//	}
//	if($("input[type='checkbox']").eq(2).prop('checked')==true)
//	{
//		od = $("label[for='od']").text();
//	}	
//	if($('#inch_yes').prop('checked')==true)
//	{
//		inch = "ТАК";
//	}
//	else
//	{
//		inch = "НІ";
//	}
//$('#mytextarea').text(moto+" на "+days+" днів\n"+email+"\nАксесуари: "+shlem+", "+bag+", "+od+"\nСтраховка: "+inch);
//}
//z6
//$("#radio").css("background-color", "red");
//$("#my_form").click(function()
//{
//	if($('#inch_yes').prop('checked')==true)
//	{
//		$("#radio").css("background-color", "#f6f6f6");
//	}
//	else
//	{
//		$("#radio").css("background-color", "red");
//	}
//});
//z7
//$("#my_form").click(function()
//{
//	var text = $("#email").val();
//	var pos = text.indexOf("Приклад: ");	
//	if(pos>=0)
//	{
//		$("#email").css("background-color", "red");
//	}
//	else
//	{
//		$("#email").css("background-color", "lightgreen");
//	}
//});




//t8
//z1
//$(".slide-btn").animate({width:'550px'}, 10000);
//z2
//$(".slide-text>h1").animate({fontSize:'550px'}, "slow");
//z3
//$(".m6").animate({marginRight:'200px', fontSize:'20px'}, "slow");
//z4
//$(".head-moto-img").click(function(){
//	var obj = $(this)
//	obj.animate({height:'300px', opacity:'0.4'},'slow');
//	obj.animate({width:'300px', opacity:'0.8'},'slow');
//	obj.animate({height:'100px', opacity:'0.4'},'slow');
//	obj.animate({width:'100px', opacity:'0.8'},'slow');
//})
//z5
//$('.slide-btn').click(function(){
//	$(this).animate({width:'400px', fontSize:'2.5em'},'slow');
//	$(".slide-btn+span").animate({height:'toggle'},'slow');
//});
//z6
//$(".blog-post-date").click(function(){
//	$('+.blog-post-info>.post-head', this).animate({marginLeft:'300px', opacity:'0.4'},'slow');
//	$(">span", this).animate({height:'120px', width:'120px'},'slow');
//});
//z7
//$(".koshik-wrapper").click(function(){
//	$(this).animate({borderLeftWidth:'10px'}, 500);
//	$(this).animate({borderTopWidth:'10px'},500);
//	$(this).animate({borderRightWidth:'10px'},500);
//	$(this).animate({borderBottomWidth:'10px'},500);
//	$(this).animate({height:'300px'},500);
//	$(this).animate({marginLeft:'100px'},500);
//	$(this).animate({width:'100px'},500);
//	$(this).animate({marginLeft:'500px'},500);
//	$(this).animate({width:'100%'},500);
//	$(this).animate({marginLeft:'0px'},500);
//})




//t9
//z1
//var fontStateP = 0;
//var fontStateM = 0;
//$('.btn-fs').click(function(){
//	var fontSize = parseInt($("body").css("font-size"));
//	if($(this).hasClass("plus-font-size"))
//	{
//		fontSize = fontSize + 1 + "px";
//		$("body").css({"font-size":fontSize});
//		fontStateP++;
//	}
//	if($(this).hasClass("minus-font-size"))
//	{
//		fontSize = fontSize - 1 + "px";
//		$("body").css({"font-size":fontSize});
//		fontStateM++;
//	}
//	if($(this).hasClass("normal-font-size"))
//	{
//		if(fontStateP>0){
//			fontSize = fontSize - fontStateP + "px";
//			$("body").css({"font-size":fontSize});
//		}if(fontStateM>0){
//			fontSize = fontSize + fontStateP + "px";
//			$("body").css({"font-size":fontSize});
//		}
//	}
//});
//z2
//$('.head-moto-img+h3+p').hide();
//$('.head-moto-img').hover(
//function()
//{
//	$('+h3+p', this).slideDown();
//},
//function()
//{
//	$('+h3+p', this).slideUp();
//});
//z3
//$("nav").css("marginRight", "400px");
//$("top-nav").animate({marginRight:'0px'});
//$(".slide-text").hide();
//$(".slide-text").slideDown(1000);
//$("h1").animate({fontSize:"70px"}, 2000);
//$(".slide-btn").animate({width:"550px", opacity:"0.8"}, 2000);
//$(".slide-btn+span").animate({marginLeft:"550px"}, 1500);
//$(".slide-btn+span").animate({marginLeft:"0px"}, 1000);
//z5
//$('#div_form_2>p>strong').first().text("Кількість товару: ");
//$('#email').val("");
//$('#email').bind("change keyup input click", function(){
//	if(this.value.match(/[^0-9]/g))
//	{
//		this.value = this.value.replace(/[^0-9]/g,'');
//	}
//	$('#div_form_2>p>strong').first().text("Кількість товару: " + this.value);
//});
//z6
//$('#my_button').click(function()
//{
//	var moto = parseInt($('#motoSelect option:selected').val());
//	var days = parseInt($('#daysSelect option:selected').text());
//	var count = parseInt($('#email').val());
//	var shlem = 0, bag = 0, od = 0, inch = 0;
//	
//	if($("input[type='checkbox']").eq(0).prop('checked')==true)
//	{
//		shlem = parseInt($("input[type='checkbox']").eq(0).val());
//	}
//	if($("input[type='checkbox']").eq(1).prop('checked')==true)
//	{
//		bag = parseInt($("input[type='checkbox']").eq(1).val());
//	}
//	if($("input[type='checkbox']").eq(2).prop('checked')==true)
//	{
//		od = parseInt$($("input[type='checkbox']").val();
//	}
//	if($('#inch_yes').prop('checked')==true)
//	{
//		inch = parseInt($("#inch_no").val());
//	}
//	else
//	{
//		inch = parseInt($("#inch_no").val());
//	}
//	
//	var sum = (moto+shlem+bag+od+inch)*day*count;
//	$('#mytextarea').text("Сума вашого замовлення: "+sum+"$" );
//})




//t10
//z1
//$('#accordion').accordion();
//z2
//$('#accordion').accordion({collapsible:true});
//z3
//var icons = {
//	header: "ui-icon-circle-arrow-e",
//	activeHeader: "ui-icon-circle-arrow-s"
//};
//$('#accordion').accordion({
//	collapsible:true,
//	icons:icons
//});
//z4
//var icons = {
//	header: "ui-icon-circle-plus",
//	activeHeader: "ui-icon-circle-minus"
//};
//$('#accordion').accordion({
//	collapsible:true,
//	icons:icons
//});
//z5.1
//var icons = {
//	header: "ui-icon-circle-plus",
//	activeHeader: "ui-icon-circle-minus"
//};
//$('#accordion').accordion({
//	collapsible:true,
//	icons:icons,
//	active:false,
//	heightStyle:"content"
//});
//z6
//var icons = {
//	header: "ui-icon-circle-plus",
//	activeHeader: "ui-icon-circle-minus"
//};
//$('#accordion2').accordion({
//	collapsible:true,
//	icons:icons,
//	active:false,
//	heightStyle:"content"
//});
//$(".categorie").show();




//t11
//z1
//$("#my_button").button();
//z2
//$("#clear_form").button();
//$("#clear_form").click(function(event)
//{
//$("#div_form1 input[type=checkbox]").removeAttr('checked');
//$("#div_form1 input[type=radio]").removeAttr('checked');
//$("input[type=text], textarea").val('');
//event.preventDefault();
//});
//z3
$("input[type=checkbox]").checkboxradio();
$("input[type=radio]").checkboxradio();
//z4
//$("#motoSelect, #daysSelect").selectmenu();
//z5
//$.widget("custom.iconselectmenu",$.ui.selectmenu,
//{
//	_renderItem:function(ul, item)
//	{
//		var li = $("<li>")
//		wrapper = $("<div>",{text:item.label});
//		
//		if (item.disable)
//		{
//			li.addClass("ui-state-disabled");
//		}		
//		$("<span>",{
//			style: item.element.attr("data-style"),
//			"class":"ui-icon" + item.element.attr("data-class")
//		}).appendTo(wrapper);
//		return li.append(wrapper).appendTo(ul);
//	}
//});
//$("#motoSelect").iconselectmenu().iconselectmenu("menuWidget").addClass("ui-menu-icons customicons")
//z6
//var circle = $("#circle");
//$("#radius").selectmenu({
//	change: function(event, data)
//	{
//		circle.css({
//			width: data.item.value,
//			height: data.item.value
//		});
//	}
//});
//
//
//$("#color").selectmenu({
//	change: function(event, data)
//	{
//		circle.css("background", data.item.value);
//	}
//});




//t12
//z1
//var handle = $("#custom-handle");
//$("#slider").slider({
//	create:function(){
//		handle.text($(this).slider("value"));
//	},
//	slide:function(event,ui){
//		handle.text(ui.value);
//		$("#mytextarea").text(ui.value + " мотоциклів");
//	}
//})
//z2
//var dateFormat = "mm/dd/yy",
//from = $("#from").datepicker({
//	defaultDate:"+1w",
//	changeMonth:true,
//	numberOfMonths:1
//})
//.on("change", function(){
//	to.datepicker("option","minDate",getDate(this));
//}),
//to = $("#to").datepicker({
//	defaultDate:"+1w",
//	changeMonth:true,
//	numberOfMonths:1
//})
//.on("change", function(){
//	from.datepicker("option","maxDate",getDate(this));
//});
//
//function getDate(element){
//	var date;
//	try{
//		date = $.datepicker.parseDate(dateFormat,element.value);	
//	}
//	catch(error)
//		{
//			date=null;
//		}
//	return date;
//}
//z3
//var days=0;
//$("#to").change(function(){
//	 var Date1 = new Date ($('.datepicker:first').val());
//	 var Date2 = new Date ($('.datepicker:last').val());
//	 var Days = Math.floor(((Date2.getTime() - Date1.getTime())/(1000*60*60*24))+1);
//	 days = Days;
//	 $("#mytextarea").text(function(i,origText){
//		 return Days + " днів" + " \n" + origText;
//	 });
//});
//z4
//$("#slider-range").slider({
//	range:true,
//	min:10,
//	max:1000,
//	values:[50,400],
//	slide: function(event,ui){
//		$("#amount").val(ui.values[0]+ ' - ' +ui.values[1]+ ' км');
//	}
//});
//$("#amount").val($("#slider-range").slider("values", 0)+ ' - '+ ("#slider-range").slider("values", 1)+ ' км');
//z5
//$("#progressbar").progressbar({value:0});
//$("#opros:radio").change(function(){
//	var chRadio = $("#opros div[id*=radio]").size();
//	$("#answerCount").text("Дано відповідей " +chRadio+ "з " +questCount);
//});
//z6

//z7
//var availableTags["Вінницька", "Волинська", "Вінницька", "Волинська", "Дніпропетровська", "Донецька", "Житомирська", "Закарпатська",  "Запорізька", "Івано-Франківська", "Київська", "Кіровоградська", "Луганська", "Львівська", "Миколаївська", "Одеська", "Полтавська", "Рівненська", "Сумська", "Тернопільська", "Харківська", "Херсонська", "Хмельницька", "Черкаська", "Чернівецька", "Чернігівська"];
//$("#tags").autocoplete({
//	source:availableTags
//});




//t13
//z1
//$("#dialog").dialog({autoOpen:true});












});