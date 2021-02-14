	$(function() {
		$("#id_hire_date_ym_disp").datepicker({
			language : 'ja',
			startView : 1,
			format : 'yyyy年mm月',
			autoclose : true,
			immediateUpdates : true,
			minViewMode : 1,
			orientation : 'bottom',
		});
	});

	// 日付表示用フォーマット(数値6桁→YYYY年MM月)
	$(window).on('load', function() {
		if($("#id_hire_date_ym").val()){
			$("#id_hire_date_ym_disp").val($("#id_hire_date_ym").val().substr(0,4)+"年"+$("#id_hire_date_ym").val().substr(4,6)+"月");
		}
	});

	// 日付form送信用フォーマット(YYYY年MM月→数値6桁)
	function funcdate() {
		$("#id_hire_date_ym").val($("#id_hire_date_ym_disp").val().replace(/[^0-9]/g, ''));
		return true;
	};