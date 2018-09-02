
        let upload = document.querySelector('#id_img');
        let fileListDom = document.querySelector('.file-list-dom');
        let fileList = {};

        let formData = new FormData();
        upload.addEventListener('change', function() {
            for (let i = this.files.length - 1; i >= 0; i--) {
                    let file = this.files[i];
                    let key = file.name;
                    let fileItem = {
                    'file': file,
                    'cover': ''
                    }
                    if (/(image\/)/.test(file.type)) {
                    let reader = new FileReader();
                    reader.readAsDataURL(file);
                    reader.onload = function() {
                    fileItem.cover = this.result;
                    fileList[key] = fileItem;
                    formData.append(key, file);
                    showFile(key, true);
                    }
                    } else {
                    fileList[key] = fileItem;
                    formData.append(key, file);

                    showFile(key, false);
                    }
                }
            });
         // 显示图片
        function showFile(key, isImg) {
            let file = document.querySelector(`[key="${key}"]`);
            if (file === null) {
                if (isImg) {
                         fileListDom.innerHTML += '<div key="' + key + '" class="pre-item"><img src="' + fileList[key].cover + '"/></div>';
                } else {
                         fileListDom.innerHTML += '<div key="' + key + '" class="pre-item">' + key + '</div>';
                }
            } else {
            file.style.display = 'block';
            }
            };
        // 触发删除事件
        fileListDom.addEventListener('click', function(e) {
                console.log(formData)
            let target = e.target || e.srcElement;
            if (target.classList.contains('pre-item')) {
            delFile(target.getAttribute('key'));
            }
            });
        // 删除图片
        function delFile(key) {
                            let file = document.querySelector(`[key="${key}"]`);
                            if (file !== null) {
                            delete fileList[key];
                            formData.delete(key);
                            file.style.display = 'none';
                            }
                };


