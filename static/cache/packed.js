/**
 * Created with Visual Form Builder by 23rd and Walnut
 * www.visualformbuilder.com
 * www.23andwalnut.com
 */


$(document).ready(function()
{
    //Style selects, checkboxes, etc
    $("select, input:checkbox, input:radio, input:file").uniform();

    //Date and Range Inputs
    $("#field13").dateinput();
    //$("#field13").rangeinput();

    /**
     * Get the jQuery Tools Validator to validate checkbox and
     * radio groups rather than each individual input
     */

    <input type="date" />
    $('[type=checkbox]').bind('change', function(){
        clearCheckboxError($(this));
    });


    //validate checkbox and radio groups
    function validateCheckRadio(){
        var err = {};

        $('.radio-group, .checkbox-group').each(function(){
             if($(this).hasClass('required'))
                if (!$(this).find('input:checked').length)
                    err[$(this).find('input:first').attr('name')] = 'Please complete this mandatory field.';
        });

        if (!$.isEmptyObject(err)){
            validator.invalidate(err);
            return false
        }
        else return true;

    }





    //clear any checkbox errors
    function clearCheckboxError(input){
        var parentDiv = input.parents('.field');

        if (parentDiv.hasClass('required'))
            if (parentDiv.find('input:checked').length > 0){
                validator.reset(parentDiv.find('input:first'));
                parentDiv.find('.error').remove();
            }
    }




    //Position the error messages next to input labels
    $.tools.validator.addEffect("labelMate", function(errors, event){
        $.each(errors, function(index, error){
            error.input.first().parents('.field').find('.error').remove().end().find('label').after('<span class="error">' + error.messages[0] + '</span>');
        });

    }, function(inputs){
        inputs.each(function(){
            $(this).parents('.field').find('.error').remove();
        });

    });


    /**
     * Handle the form submission, display success message if
     * no errors are returned by the server. Call validator.invalidate
     * otherwise.
     */

    $(".TTWForm").validator({effect:'labelMate'}).submit(function(e){
       var form = $(this), checkRadioValidation = validateCheckRadio();

        if(!e.isDefaultPrevented() && checkRadioValidation){
            $.post(form.attr('action'), form.serialize(), function(data){
                data = $.parseJSON(data);

                if(data.status == 'success'){
                    form.fadeOut('fast', function(){
                        $('.TTWForm-container').append('<h2 class="success-message">Success!</h2>');
                    });
                }
                else validator.invalidate(data.errors);

            });
        }

        return false;
    });

    var validator = $('.TTWForm').data('validator');


});

$(document).ready(function(){
$("#form :input[type='text']").tooltip({
        position: "center right",
        offset: [-2, 10],
        effect: "fade",
        opacity: 0.7
    });
});

/*
	HUMANIZED MESSAGES 1.0
	idea - http://www.humanized.com/weblog/2006/09/11/monolog_boxes_and_transparent_messages
	home - http://humanmsg.googlecode.com
*/

var humanMsg = {
	setup: function(appendTo, logName, msgOpacity) {
		humanMsg.msgID = 'humanMsg';
		humanMsg.logID = 'humanMsgLog';

		// appendTo is the element the msg is appended to
		if (appendTo == undefined)
			appendTo = 'body';

		// The text on the Log tab
		if (logName == undefined)
			logName = 'Message Log';

		// Opacity of the message
		humanMsg.msgOpacity = .8;

		if (msgOpacity != undefined) 
			humanMsg.msgOpacity = parseFloat(msgOpacity);

		// Inject the message structure
		jQuery(appendTo).append('<div id="'+humanMsg.msgID+'" class="humanMsg"><div class="round"></div><p></p><div class="round"></div></div> <div id="'+humanMsg.logID+'"><p>'+logName+'</p><ul></ul></div>')
		
		jQuery('#'+humanMsg.logID+' p').click(
			function() { jQuery(this).siblings('ul').slideToggle() }
		)
	},

	displayMsg: function(msg) {
		if (msg == '')
			return;

		clearTimeout(humanMsg.t2);

		// Inject message
		jQuery('#'+humanMsg.msgID+' p').html(msg)
	
		// Show message
		jQuery('#'+humanMsg.msgID+'').show().animate({ opacity: humanMsg.msgOpacity}, 200, function() {
			jQuery('#'+humanMsg.logID)
				.show().children('ul').prepend('<li>'+msg+'</li>')	// Prepend message to log
				.children('li:first').slideDown(200)				// Slide it down
		
			if ( jQuery('#'+humanMsg.logID+' ul').css('display') == 'none') {
				jQuery('#'+humanMsg.logID+' p').animate({ bottom: 40 }, 200, 'linear', function() {
					jQuery(this).animate({ bottom: 0 }, 300, 'easeOutBounce', function() { jQuery(this).css({ bottom: 0 }) })
				})
			}
			
		})

		// Watch for mouse & keyboard in .5s
		humanMsg.t1 = setTimeout("humanMsg.bindEvents()", 700)
		// Remove message after 5s
		humanMsg.t2 = setTimeout("humanMsg.removeMsg()", 5000)
	},

	bindEvents: function() {
	// Remove message if mouse is moved or key is pressed
		jQuery(window)
			.mousemove(humanMsg.removeMsg)
			.click(humanMsg.removeMsg)
			.keypress(humanMsg.removeMsg)
	},

	removeMsg: function() {
		// Unbind mouse & keyboard
		jQuery(window)
			.unbind('mousemove', humanMsg.removeMsg)
			.unbind('click', humanMsg.removeMsg)
			.unbind('keypress', humanMsg.removeMsg)

		// If message is fully transparent, fade it out
		if (jQuery('#'+humanMsg.msgID).css('opacity') == humanMsg.msgOpacity)
			jQuery('#'+humanMsg.msgID).animate({ opacity: 0 }, 500, function() { jQuery(this).hide() })
	}
};

jQuery(document).ready(function(){
	humanMsg.setup();
})