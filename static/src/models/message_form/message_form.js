odoo.define('zalo_message/static/src/models/message_form/message_form.js', function (require) {
    'use strict';

    const aaa = require('mail/static/src/components/chatter_topbar/chatter_topbar.js');
    console.log(aaa)

    aaa.include({
        _onClickSendZaloMessage() {
            console.log('click');
        }
    });

});

