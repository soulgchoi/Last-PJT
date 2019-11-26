const likeButtons = document.querySelectorAll('.js-like-button');

likeButtons.forEach((likeButton) => {
    likeButton.addEventListener('click', function(event) {
        // console.log(event.target.dataset.id) // data-id = posting.id 가져오는중
        const URL = `/insta/${event.target.dataset.id}/like/`;
        // POST 요청 받기
        axios.defaults.xsrfCookieName = 'csrftoken'  // xsrf = csrf
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'
        // axios.get(URL)
        axios.post(URL)
            .then((res) => {
                if (res.data.liked) {  // 지금 좋아요가 끝났다면
                    event.target.classList.remove('far');
                    event.target.classList.add('fas');
                } else {  // 지금 좋아요 취소했다면
                    event.target.classList.remove('fas');
                    event.target.classList.add('far');
                }
            })
    })
}) 
