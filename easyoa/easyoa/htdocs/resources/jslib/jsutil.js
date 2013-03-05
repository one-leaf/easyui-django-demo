/**
 * @author 孙宇
 * 
 * @requires jQuery,EasyUI
 * 
 * panel关闭时回收内存，主要用于layout使用iframe嵌入网页时的内存泄漏问题
 */
$.fn.panel.defaults.onBeforeDestroy = function() {
    var frame = $('iframe', this);
    try {
        if (frame.length > 0) {
            for (var i = 0; i < frame.length; i++) {
                frame[i].contentWindow.document.write('');
                frame[i].contentWindow.close();
            }
            frame.remove();
            if ($.browser.msie) {
                CollectGarbage();
            }
        }
    } catch (e) {
    }
};

/**
 * 使panel和datagrid在加载时提示
 * 
 * @author 孙宇
 * 
 * @requires jQuery,EasyUI
 * 
 */
$.fn.panel.defaults.loadingMessage = '加载中....';
$.fn.datagrid.defaults.loadMsg = '加载中....';

/**
 * 
 * @requires jQuery,EasyUI
 * 
 * 扩展validatebox，添加验证两次密码功能
 */
$.extend($.fn.validatebox.defaults.rules, {
    eqPwd: {
        validator: function(value, param) {
            return value == $(param[0]).val();
        },
        message: '密码不一致！'
    }
});

$.fn.datebox.defaults.formatter = function(date) {
//	var y = date.getFullYear();
//	var m = date.getMonth()+1;
//	var d = date.getDate();
//	return m+'/'+d+'/'+y;
    var y = date.getFullYear();
    var m = date.getMonth() + 1;
    var d = date.getDate();
    return y + '-' + (m < 10 ? ('0' + m) : m) + '-' + (d < 10 ? ('0' + d) : d);
};

$.fn.datebox.defaults.parser = function(s) {
//    var t = Date.parse(s);
//    if (!isNaN(t)) {
//        return new Date(t);
//    } else {
//        return new Date();
//    }
    if (!s)
        return new Date();
    var ss = (s.split('-'));
    var y = parseInt(ss[0], 10);
    var m = parseInt(ss[1], 10);
    var d = parseInt(ss[2], 10);
    if (!isNaN(y) && !isNaN(m) && !isNaN(d)) {
        return new Date(y, m - 1, d);
    } else {
        return new Date();
    }
};

$.fn.tree.defaults.loadFilter = function(data, parent) {
    var opt = $(this).data().tree.options;
    var idFiled, textFiled, parentField;
    if (opt.parentField) {
        idFiled = opt.idFiled || 'id';
        textFiled = opt.textFiled || 'text';
        parentField = opt.parentField;
        var i, l, treeData = [], tmpMap = [];
        for (i = 0, l = data.length; i < l; i++) {
            tmpMap[data[i][idFiled]] = data[i];
        }
        for (i = 0, l = data.length; i < l; i++) {
            if (tmpMap[data[i][parentField]] && data[i][idFiled] != data[i][parentField]) {
                if (!tmpMap[data[i][parentField]]['children'])
                    tmpMap[data[i][parentField]]['children'] = [];
                data[i]['text'] = data[i][textFiled];
                tmpMap[data[i][parentField]]['children'].push(data[i]);
            } else {
                data[i]['text'] = data[i][textFiled];
                treeData.push(data[i]);
            }
        }
        return treeData;
    }
    return data;
};

/**
 * 
 * @requires jQuery,EasyUI
 * 
 * 防止panel/window/dialog组件超出浏览器边界
 * @param left
 * @param top
 */
var easyuiPanelOnMove = function(left, top) {
    var l = left;
    var t = top;
    if (l < 1) {
        l = 1;
    }
    if (t < 1) {
        t = 1;
    }
    var width = parseInt($(this).parent().css('width')) + 14;
    var height = parseInt($(this).parent().css('height')) + 14;
    var right = l + width;
    var buttom = t + height;
    var browserWidth = $(window).width();
    var browserHeight = $(window).height();
    if (right > browserWidth) {
        l = browserWidth - width;
    }
    if (buttom > browserHeight) {
        t = browserHeight - height;
    }
    $(this).parent().css({/* 修正面板位置 */
        left: l,
        top: t
    });
};
$.fn.dialog.defaults.onMove = easyuiPanelOnMove;
$.fn.window.defaults.onMove = easyuiPanelOnMove;
$.fn.panel.defaults.onMove = easyuiPanelOnMove;

/**
 * 
 * @requires jQuery
 * 
 * 将form表单元素的值序列化成对象
 * 
 * @returns object
 */
serializeObject = function(form) {
    var o = {};
    $.each(form.serializeArray(), function(index) {
        if (o[this['name']]) {
            o[this['name']] = o[this['name']] + "," + this['value'];
        } else {
            o[this['name']] = this['value'];
        }
    });
    return o;
};



/**
 * 
 * @requires jQuery,EasyUI
 * 
 * @param options
 */
dialog = function(options) {
    var opts = $.extend({
        modal: true,
        onClose: function() {
            $(this).dialog('destroy');
        }
    }, options);
    return $('<div/>').dialog(opts);
};

dialogFrame = function(id,src,options) {
    var opts = $.extend({
	modal : true,
        content: '<iframe id="'+id+'" src="'+src+'" frameborder="0" style="border:0;width:100%;height:99%;" scrolling="no"></iframe>',
	onClose : function() {
		$(this).dialog('destroy');
	}
    }, options);
    //var f=$('<iframe id="'+id+'" src="'+src+'" frameborder="0" style="border:0;width:100%;height:99.4%;"></iframe>');
    var d= $('<div/>').dialog(opts);
    //d.data().window.shadow.append('<iframe width="100%" height="100%" frameborder="0" scrolling="no"></iframe>');
    return d;
};

/**
 * @author 鸵鸟
 * 
 * @requires jQuery,EasyUI
 * 
 * @param title
 *            标题
 * 
 * @param msg
 *            提示信息
 * 
 * @param fun
 *            回调方法
 */
messagerConfirm = function(title, msg, fn) {
    return $.messager.confirm(title, msg, fn);
};

/**
 * @author 鸵鸟
 * 
 * @requires jQuery,EasyUI
 */
messagerShow = function(options) {
    return $.messager.show(options);
};

/**
 * @author 鸵鸟
 * 
 * @requires jQuery,EasyUI
 */
messagerAlert = function(title, msg, icon, fn) {
    return $.messager.alert(title, msg, icon, fn);
};

/**
 * @author 鸵鸟
 * 
 * @requires jQuery,EasyUI
 */
getFrameWindow = function() {
    var tab = centerTabs.tabs('getSelected');
    var tbIframe = tab.find('iframe')[0];
    console.info(tbIframe);
    console.info(tbIframe.contentWindow);
    return tbIframe.contentWindow;
};


getFrameComponent = function(id) {
    var tab = centerTabs.tabs('getSelected');
    var tbIframe = tab.find('iframe')[0];
    var comp = tbIframe.contentWindow.$(tbIframe).contents().find(id);
    return comp;
};
