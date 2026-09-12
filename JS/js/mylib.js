//$(function()
//{
//t1
//z1
//alert($('h1').text());




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




//});