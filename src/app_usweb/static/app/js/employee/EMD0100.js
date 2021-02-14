	$(function() {
		$("#hireDate").datepicker({
			language : 'ja',
			startView : 1,
			format : 'yyyy年mm月',
			autoclose : true,
			immediateUpdates : true,
			minViewMode : 1,
			orientation : 'bottom',
		});
	});
	$(function() {
		  $('.btn-del').on('click', function () {
		     $("#del_pk").text($(this).data("pk"));
		     $('#del_url').attr('href', $(this).data("url"));
		  });
		});

	// 日付表示用フォーマット(数値6桁→YYYY年MM月)
	$(window).on('load', function() {
			$('.date').each(function(i, elem) {
				if (i !== 0){
					let txtDate = elem.innerText;
					elem.innerText = txtDate.substr(0,4)+"年"+txtDate.substr(4,6)+"月";
				}
			})
	});