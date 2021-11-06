$(document).ready(function () {
    /**
     @todo 获取三个下拉框
     */
    var collegeName = $(".collegeName").children("select");
    var majorName = $(".majorName").children("select");
    var className = $(".className").children("select");

    /**
     @todo 给三个下拉框加下拉框的改变事件
     */
    collegeName.change(function () {
        //获取学院下拉框选中的值
        var collegeValue = $(this).val();
        if (collegeValue === 'agri_college') {
            majorName.html("<option value='selected'>请选择专业方向</option><option value='agriculture'>农学</option><option value='plant_protection'>植物保护</option>");
        }
        if (collegeValue === 'garden_art') {
            majorName.html("<option value='selected'>请选择专业方向</option><option value='horticulture'>园艺</option>");
        }
        //此处添加其他还未写完的代码
    });

    majorName.change(function () {
        //获取专业方向下拉框选中的值
        var majorValue = $(this).val();
        if (majorValue === 'agriculture') {
            className.html("<option value='1001'>1001</option><option value='1101'>1101</option>");
        }
        if (majorValue === 'plant_protection') {
            className.html("<option value='1001'>0902</option><option value='1101'>1102</option>");
        }
        if (majorValue === 'horticulture') {
            className.html("<option value='1001'>1002</option><option value='1101'>1103</option>");
        }
        //...
    });

    /**
     @todo 设置表格的隐藏和显示切换
     */
    $("#softvareId").click(function () {
        $("#1101tr").slideToggle();
    });

    $("#1101td").click(function () {
        $("#1101table").slideToggle();
    });

    $("#rank").change(function () {


        //获取专业方向下拉框选中的值
        var rank = $(this).val();
        window.location.href = "/student/searchinfo/" + "?rank=" + rank;
    });

    $("#ssave").click(function () {

        $fom = $('#tableedit');
        var data = $fom.serialize();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            cache: false,
            type: 'post',
            dataType: 'json',
            url: "/student/studetail/",
            data: {'data': data, 'csrfmiddlewaretoken': token},
            async: false,
            success: function (data) {
                if (data.status == 'success') {
                    alert('修改成功!')
                    window.location.reload()
                }
            }
        })
    });

    $("#sdelete").click(function () {
        $fom = $('#tableedit');
        var data = $fom.serialize();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            cache: false,
            type: 'post',
            dataType: 'json',
            url: "/student/studetail/",
            data: {'data': data, 'is_delete': true, 'csrfmiddlewaretoken': token},
            async: false,
            success: function (data) {
                if (data.status == 'success') {
                    alert('删除成功');
                    window.location.reload()
                }
            }
        })
    });

    $("#btn_import_paper").click(function () {
         var token = $('input[name=csrfmiddlewaretoken]').val()
            var fileobj = $('#paper_file')[0].files[0];   //先将jquery对象转换为dom对象
            var form = new FormData();
            form.append('paper_file',fileobj);
          $.ajax({
            url: '/student/stuaexdd/',
            data: form,
            processData:false,
            contentType:false,
            type: 'post',
              headers:{ "X-CSRFtoken":token},
              success:function (data) {
                console.log(data)
                  if(data.status=='f'){
                      console.log(data.msg)
                      alert(data.msg)
                  }
                  else{
                      alert('成功')
                      window.location.reload()
                  }
              }
          }).done(function(response, textStatus, jqXHR){ //same as .success (depricated as of 1.8)

          })
          .fail(function(jqXHR, textStatus, errorThrown){ //replaces .error

          })
          .always(function(/*data|jqXHR, textStatus, jqXHR|errorThrown*/){ //replaces .complete

          });
        });

});

/**
 @todo 响应高级搜索按钮触发事件
 */
function advanceSearch() {

};

/**
 @todo 响应导出按钮触发事件
 */
function exportData() {

    $fom = $('#fom')
    data = $fom.serialize()

    window.location.href = "/student/export/xls/" + "?data=" + data;
};


/**

 */
var menuids = ["suckertree1"];


function buildsubmenus() {
            for (var i = 0; i < menuids.length; i++) {
                var ultags = document.getElementById(menuids[i]).getElementsByTagName(
                    "ul")
                for (var t = 0; t < ultags.length; t++) {
                    ultags[t].parentNode.getElementsByTagName("a")[0].className = "subfolderstyle"
                    ultags[t].parentNode.onmouseover = function () {
                        this.getElementsByTagName("ul")[0].style.display = "block"
                    }
                    ultags[t].parentNode.onmouseout = function () {
                        this.getElementsByTagName("ul")[0].style.display = "none"
                    }
                }
            }
}

if (window.addEventListener) {
    window.addEventListener("load", buildsubmenus, false);
}
else if (window.attachEvent) {
    window.attachEvent("onload", buildsubmenus);
}

/**
 @todo 响应审核按钮触发的事件
 */
function check() {

};


/**
 @todo 响应编辑按钮，显示保存按钮
 */
function edit(id) {
    if (document.getElementById(id).style.display === "none") {
        document.getElementById(id).style.display = "block";
    } else {
        document.getElementById(id).style.display = "none"
    }
};

/**
 @todo 弹出框响应函数
 */
function popupp(div1, div2, btnId, i) {
    if (i === null)
        i = '';
    var resp = $.ajax({
        cache: false,
        type: 'get',
        dataType: 'json',
        url: "/student/studetail/",
        data: {'data': i},
        async: false,
    }).responseText;
    $("#ffff").html(resp)

    $(div1).css({display: "block", height: $(document).height()});
    var yscroll = document.documentElement.scrollTop;
    $(div2).css("top", "100px");
    $(div2).css("display", "block");
    document.documentElement.scrollTop = 0;

    $(btnId).click(function () {
        $(div1).css("display", "none");
        $(div2).css("display", "none");
    });
};


/**
 @todo 响应保存按钮事件
 */
function save(id) {
    document.getElementById(id).style.display = "none";
};

/**
 @todo 手动录入按钮响应事件
 */
function manually() {
    //先弹出输入提示框，用来生成要生成的空白记录数量
    var iMsg = prompt("请输入要录入的记录数", "");
    if (iMsg === "" || iMsg === "undefined" || iMsg === undefined) {
        alert('请输入数字');
    }
    else {
        /*根据输入框中的值生成相应的空白记录*/

        //先得到要隐藏的节点的父节点
        var oParentNode = document.getElementById("liulanbiao").parentNode;

        //先将当前页面中的表格隐藏
        document.getElementById("liulanbiao").style.display = "none";

        //创建一个div元素节点
        var oDiv = document.createElement("div");
        oDiv.id = "liulanbiao";
        oDiv.style = "display: block, margin-left: 10px";

        oParentNode.appendChild(oDiv);


        //在隐藏节点下添加空白记录
        var oTable = document.createElement("table");//创建table元素节点
        /*给table添加特性值*/
        oTable.setAttribute("id", "currentTable");
        oTable.setAttribute("style", "dispaly: block");
        oTable.setAttribute("width", "99%");
        oTable.setAttribute("border", "0");
        oTable.setAttribute("cellspacing", "0");
        oTable.setAttribute("cellpadding", "0");
        oTable.setAttribute("class", "CContent");
        oDiv.appendChild(oTable);


        oTable.insertRow(0);
        oTable.rows[0].insertCell(0);
        var oTableTrTd = oTable.rows[0].cells[0]
        oTableTrTd.setAttribute("class", "CPanel");//在这个<td>里面加入一个表格

        var oTableOuter = document.createElement("table");
        oTableOuter.setAttribute("width", "96%");
        oTableOuter.setAttribute("border", "0");
        oTableOuter.setAttribute("cellspacing", "0");
        oTableOuter.setAttribute("cellpadding", "0");
        oTableOuter.setAttribute("align", "center");

        oTableTrTd.appendChild(oTableOuter);

        oTableOuter.insertRow(0);
        oTableOuter.rows[0].insertCell(0);
        var oTableOuterTrTd = oTableOuter.rows[0].cells[0];
        oTableOuterTrTd.setAttribute("height", "40");
        oTableOuterTrTd.setAttribute("class", "font42");


        var oTableTeacher = document.createElement("table");
        oTableTeacher.setAttribute("id", "tableID");
        oTableTeacher.setAttribute("bgcolor", "#464646");
        oTableTeacher.setAttribute("width", "100%");
        oTableTeacher.setAttribute("border", "0");
        oTableTeacher.setAttribute("cellspacing", "0");
        oTableTeacher.setAttribute("cellpadding", "0");
        oTableTeacher.setAttribute("class", "demo");

        oTableOuterTrTd.appendChild(oTableTeacher);

        /*第一行：表头*/
        oTableTeacher.insertRow(0);
        var oTeacherTr1 = oTableTeacher.rows[0];
        oTeacherTr1.setAttribute("class", "CTitle");

        oTeacherTr1.insertCell(0);
        var oTeacherTr1Td = oTeacherTr1.cells[0];
        oTeacherTr1Td.setAttribute("height", "22");
        oTeacherTr1Td.setAttribute("colspan", "12");
        oTeacherTr1Td.setAttribute("align", "center");
        oTeacherTr1Td.setAttribute("style", "font-size: 16px");
        oTeacherTr1Td.appendChild(document.createTextNode("教师基本信息录入表"));

        /*第二行：字段名*/
        oTableTeacher.insertRow(1);
        var oTeacherTr2 = oTableTeacher.rows[1];
        oTeacherTr2.setAttribute("bgcolor", "#EEEEEE");

        /*第一列*/
        oTeacherTr2.insertCell(0);
        var oTeacherTr2Td1 = oTeacherTr2.cells[0];
        oTeacherTr2Td1.setAttribute("width", "10%");
        oTeacherTr2Td1.appendChild(document.createTextNode("教师编号"));

        /*第二列*/
        oTeacherTr2.insertCell(1);
        var oTeacherTr2Td2 = oTeacherTr2.cells[1];
        oTeacherTr2Td2.setAttribute("width", "7%");
        oTeacherTr2Td2.appendChild(document.createTextNode("姓名"));

        /*第三列*/
        oTeacherTr2.insertCell(2);
        var oTeacherTr2Td3 = oTeacherTr2.cells[2];
        oTeacherTr2Td3.setAttribute("width", "7%");
        oTeacherTr2Td3.appendChild(document.createTextNode("性别"));

        /*第四列*/
        oTeacherTr2.insertCell(3);
        var oTeacherTr2Td4 = oTeacherTr2.cells[3];
        oTeacherTr2Td4.setAttribute("width", "7%");
        oTeacherTr2Td4.appendChild(document.createTextNode("民族"));

        /*第五列*/
        oTeacherTr2.insertCell(4);
        var oTeacherTr2Td5 = oTeacherTr2.cells[4];
        oTeacherTr2Td5.setAttribute("width", "7%");
        oTeacherTr2Td5.appendChild(document.createTextNode("籍贯"));

        /*第六列*/
        oTeacherTr2.insertCell(5);
        var oTeacherTr2Td6 = oTeacherTr2.cells[5];
        oTeacherTr2Td6.setAttribute("width", "7%");
        oTeacherTr2Td6.appendChild(document.createTextNode("部门"));

        /*第七列*/
        oTeacherTr2.insertCell(6);
        var oTeacherTr2Td7 = oTeacherTr2.cells[6];
        oTeacherTr2Td7.setAttribute("width", "10%");
        oTeacherTr2Td7.appendChild(document.createTextNode("在岗职位"));

        /*第八列*/
        oTeacherTr2.insertCell(7);
        var oTeacherTr2Td7 = oTeacherTr2.cells[7];
        oTeacherTr2Td7.setAttribute("width", "10%");
        oTeacherTr2Td7.appendChild(document.createTextNode("教师职称"));

        /*第九列*/
        oTeacherTr2.insertCell(8);
        var oTeacherTr2Td8 = oTeacherTr2.cells[8];
        oTeacherTr2Td8.setAttribute("width", "10%");
        oTeacherTr2Td8.appendChild(document.createTextNode("职称评定时间"));

        /*第十列*/
        oTeacherTr2.insertCell(9);
        var oTeacherTr2Td9 = oTeacherTr2.cells[9];
        oTeacherTr2Td9.setAttribute("width", "10%");
        oTeacherTr2Td9.appendChild(document.createTextNode("工作时间"));

        /*第十一列*/
        oTeacherTr2.insertCell(10);
        var oTeacherTr2Td11 = oTeacherTr2.cells[10];
        oTeacherTr2Td11.setAttribute("width", "7%");
        oTeacherTr2Td11.appendChild(document.createTextNode("学历"));

        /*第十二列*/
        oTeacherTr2.insertCell(11);
        var oTeacherTr2Td12 = oTeacherTr2.cells[11];
        oTeacherTr2Td12.setAttribute("width", "14%");
        oTeacherTr2Td12.appendChild(document.createTextNode("操作"));


        /*根据输入的数值产生相应数量的空白记录*/
        for (var i = 0, iNum = parseInt(iMsg); i < iNum; i++) {
            oTableTeacher.insertRow(i + 2);
            var oTeacherTri = oTableTeacher.rows[i + 2];
            if ((i % 2) === 0) {
                oTeacherTri.setAttribute("bgcolor", "#FFFFFF");
            } else {
                oTeacherTri.setAttribute("bgcolor", "#EEEEEE");
            }

            /*第一列*/
            oTeacherTri.insertCell(0);
            var oTeacherTriTd1 = oTeacherTri.cells[0];
            oTeacherTriTd1.setAttribute("width", "10%");
            var tec_No = document.createElement('input');
            tec_No.type = "text";
            tec_No.size = "5";
            oTeacherTriTd1.appendChild(tec_No);

            /*第二列*/
            oTeacherTri.insertCell(1);
            var oTeacherTriTd2 = oTeacherTri.cells[1];
            oTeacherTriTd2.setAttribute("width", "7%");
            var tec_Name = document.createElement('input');
            tec_Name.type = "text";
            tec_Name.size = "5";
            oTeacherTriTd2.appendChild(tec_Name);

            /*第三列*/
            oTeacherTri.insertCell(2);
            var oTeacherTriTd3 = oTeacherTri.cells[2];
            oTeacherTriTd3.setAttribute("width", "7%");
            var tec_Sex = document.createElement('select');
            var man = document.createElement("option");
            man.appendChild(document.createTextNode("男"));
            var woman = document.createElement("option");
            woman.appendChild(document.createTextNode("女"));
            tec_Sex.appendChild(man);
            tec_Sex.appendChild(woman);
            oTeacherTriTd3.appendChild(tec_Sex);


            /*第四列*/
            oTeacherTri.insertCell(3);
            var oTeacherTriTd4 = oTeacherTri.cells[3];
            oTeacherTriTd4.setAttribute("width", "7%");
            var tec_Nation = document.createElement('select');
            var han = document.createElement("option");
            han.appendChild(document.createTextNode("汉族"));
            var daizu = document.createElement("option");
            daizu.appendChild(document.createTextNode("傣族"));
            tec_Nation.appendChild(han);
            tec_Nation.appendChild(daizu);
            oTeacherTriTd4.appendChild(tec_Nation);


            /*第五列*/
            oTeacherTri.insertCell(4);
            var oTeacherTriTd5 = oTeacherTri.cells[4];
            oTeacherTriTd5.setAttribute("width", "7%");
            var tec_Native = document.createElement('input');
            tec_Native.type = "text";
            tec_Native.size = "5";
            oTeacherTriTd5.appendChild(tec_Native);


            /*第六列*/
            oTeacherTri.insertCell(5);
            var oTeacherTriTd6 = oTeacherTri.cells[5];
            oTeacherTriTd6.setAttribute("width", "7%");
            var tec_Department = document.createElement('input');
            tec_Department.type = "text";
            tec_Department.size = "5";
            oTeacherTriTd6.appendChild(tec_Department);


            /*第七列*/
            oTeacherTri.insertCell(6);
            var oTeacherTriTd7 = oTeacherTri.cells[6];
            oTeacherTriTd7.setAttribute("width", "10%");
            var tec_Position = document.createElement('input');
            tec_Position.type = "text";
            tec_Position.size = "5";
            oTeacherTriTd7.appendChild(tec_Position);

            /*第八列*/
            oTeacherTri.insertCell(7);
            var oTeacherTriTd8 = oTeacherTri.cells[7];
            oTeacherTriTd8.setAttribute("width", "10%");
            var tec_Title = document.createElement('input');
            tec_Title.type = "text";
            tec_Title.size = "5";
            oTeacherTriTd8.appendChild(tec_Title);

            /*第九列*/
            oTeacherTri.insertCell(8);
            var oTeacherTriTd9 = oTeacherTri.cells[8];
            oTeacherTriTd9.setAttribute("width", "10%");
            var tec_Time = document.createElement('input');
            tec_Time.type = "text";
            tec_Time.size = "5";
            oTeacherTriTd9.appendChild(tec_Time);


            /*第十列*/
            oTeacherTri.insertCell(9);
            var oTeacherTriTd10 = oTeacherTri.cells[9];
            oTeacherTriTd10.setAttribute("width", "10%");
            var tec_WorkTime = document.createElement('input');
            tec_WorkTime.type = "text";
            tec_WorkTime.size = "5";
            oTeacherTriTd10.appendChild(tec_WorkTime);

            /*第十一列*/
            oTeacherTri.insertCell(10);
            var oTeacherTriTd11 = oTeacherTri.cells[10];
            oTeacherTriTd11.setAttribute("width", "7%");
            var tec_Background = document.createElement('input');
            tec_Background.type = "text";
            tec_Background.size = "5";
            oTeacherTriTd11.appendChild(tec_Background);

            /*第十二列*/
            oTeacherTri.insertCell(11);
            var oTeacherTriTd12 = oTeacherTri.cells[11];
            oTeacherTriTd12.setAttribute("width", "14%");
            var tec_Modify = document.createElement('input');
            tec_Modify.type = 'button';
            tec_Modify.value = '修改';
            var tec_Delete = document.createElement('input');
            tec_Delete.type = 'button';
            tec_Delete.value = '删除';

            oTeacherTriTd12.appendChild(tec_Modify);
            oTeacherTriTd12.appendChild(document.createTextNode(''));
            oTeacherTriTd12.appendChild(tec_Delete);

        }


        document.body.appendChild(oDiv);

    }
};


function Search() {

    var _self = $(this),
        $fom = $('#fom')

    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        cache: false,
        type: 'get',
        dataType: 'json',
        url: "/student/searchinfo",
        data: {'data': $fom.serialize(), 'csrfmiddlewaretoken': token},
        async: true,
    });


}

function ModifyPw() {

    $fom = $('#modifyform')
    var token = $('input[name=csrfmiddlewaretoken]').val();

    var newPassword = $("#newPassword").val()
    var confirmPassword = $("#confirmPassword").val()

    if (confirmPassword == '' || confirmPassword == null || confirmPassword == 'undefined') {
        alert('密码不能为空');
        return false
    }
    if (newPassword == '' || newPassword == null || newPassword == 'undefined') {
        alert('密码不能为空');
        return false
    }
    $.ajax({
        cache: false,
        type: 'POST',
        dataType: 'json',
        url: "/student/modifypassworld/",
        data: {'data': $fom.serialize(), 'csrfmiddlewaretoken': token},
        async: true,
        success: function (data) {

            if (data.status == 'fail') {
                alert('修改失败')
            } else {
                alert('修改成功')
            }
        }


    });
};


function sedit() {

    if (document.getElementById("ssave").style.display === "none") {
        document.getElementById("ssave").style.display = "block";
        var b = document.getElementsByTagName("input");
        for (var i = 0; i < b.length; i++) {
            b[i].readOnly = false;
            b[i].style.background = "0FC5FF";

        }
    } else {
        document.getElementById("ssave").style.display = "none"
    }
};

function Add() {

    var _self = $(this),
        $editMsg = $('#editMsgs');
    var table = document.getElementById("entryStuBasicInfo");
    var rows = table.rows;//获取所有行

    var ldata = []
    for (var i = 1; i < rows.length; i++) {
        if (rows[i].className == 'dere') {
            var datas = []
            for (var col = 0; col < rows[i].cells.length; col++) {
                var s = rows[i].cells[col].childNodes[0];

                ss = rows[i].cells[col].childNodes[0].value;
                if (ss=="" || ss==null || ss=="undefined"){
                    alert('数据不能为空')
                    return false
                }

                datas.push(ss)

            }
            ldata.push(datas)


        }

    }


    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        type:"POST",
        dataType: 'json',
        url: "/student/stuadd/",
        data: {"datats":JSON.stringify(ldata),'csrfmiddlewaretoken': token
        },


        success:function (data) {
           if (data.status){
               alert("添加成功！")
               window.location.reload()
           }
        }
    });

}


function manuallyexcel(div1, div2, btnId) {
    $(div1).css({display: "block", height: $(document).height()});
    var yscroll = document.documentElement.scrollTop;
    $(div2).css("top", "100px");
    $(div2).css("display", "block");
    document.documentElement.scrollTop = 0;

    $(btnId).click(function () {
        $(div1).css("display", "none");
        $(div2).css("display", "none");
    });
};