function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    console.log(parentId);
    $.get('/article/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        console.log(res);
        location.reload();
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}

function addProductToOrder(productId) {
    const prosuctcount =$('#productcount').val();
    $.get('/order/add_to-order?product_id=' + productId + '&count=' + prosuctcount).then(res =>{
        console.log(res)
    });
        }