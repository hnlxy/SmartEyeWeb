document.addEventListener('DOMContentLoaded', function() {
    // 选择全选勾选框
    var checkAllBox = document.getElementById('checkAll');

    // 选择所有行的勾选框
    var checkboxes = document.querySelectorAll('.checkItem');

    // 为全选勾选框添加事件监听
    checkAllBox.addEventListener('change', function() {
        checkboxes.forEach(function(checkbox) {
            checkbox.checked = checkAllBox.checked;
        });
    });

    // 检查是否所有行的勾选框都被选中
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            checkAllBox.checked = Array.from(checkboxes).every(c => c.checked);
        });
    });
});
