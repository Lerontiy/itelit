$(function(){
	
	$("#draggable1").draggable();
	$("#draggable2").draggable();
	$("#draggable3").draggable();
	$("#draggable4").draggable();
	
	$(".koshik-wrapper").droppable({
		drop:function(event,ui){
			$(".koshik-wrapper").addClass("ui-state-highlight")
		}});
});