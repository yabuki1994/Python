var MESSAGE = {
   ERR001 : "対象のデータが存在しません。",
   ERR002 : "必須項目を入力してください。",
   ERR003 : "入力された社員番号は既に存在しています。",
   ERR004 : "モニターコードは数字で入力してください。",
   ERR005 : "社員番号は数字で入力してください。",
   ERR006 : "導入年月日にエラーがあります。",
   ERR007 : "{0}マスタが存在しません。",
   ERR008 : "契約期間に誤りがあります。",
   INF001 : "登録しますか？",
   INF002 : "更新しますか？",
   INF003 : "{0}を削除しますか？",
   INF004 : "登録が完了しました。",
   INF005 : "更新が完了しました。",
   INF006 : "削除が完了しました。",

};

/******************************************************
* 共通処理
******************************************************/
//カレンダー表示　初期画面
$(function () {
	$("#datepicker").datepicker({
		language:'ja',
		orientation: 'bottom'		
	});
	$("#datepicker2").datepicker({
		language:'ja',
		orientation:'bottom'
	});
});

//カレンダー表示　登録処理後画面
function datepicker(date) {
	$("#datepicker").datepicker({
		language:'ja',
		orientation: 'bottom'
	});
	$("#datepicker2").datepicker({
		language:'ja',
		orientation:'bottom'
	});
	return date;
};

// URL加工
function getContextUrl(url) {
	var contextPath = $("#contextPath").val();
	return contextPath + url
}

//ボタン押下時スクロールトップ処理
function scrollTop(scr){
	$("html, body").animate({scrollTop:0},'fast');
	return scr;
}
			