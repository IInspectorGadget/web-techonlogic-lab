$(document).ready(function(){
    $('.header__burger').click(function(event){
        $('.header__burger,.nav__js,.profile__opinion,.slick-arrow,.login,.admin-panel').toggleClass('active');
        $('body').toggleClass('lock');
    });
});