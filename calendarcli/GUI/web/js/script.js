var selectedDate = new Date();
console.log(selectedDate);
jQuery(document).ready(function () {
    jQuery('.datetimepicker').datepicker({
        timepicker: true,
        language: 'en',
        range: true,
        multipleDates: true,
        multipleDatesSeparator: " - "
    });
    jQuery("#add-event").submit(function () {
        alert("Submitted");
        var values = {};
        $.each($('#add-event').serializeArray(), function (i, field) {
            values[field.name] = field.value;
        });
        console.log(
            values
        );
        return false;
    });
});

(function () {
    'use strict';
    // ------------------------------------------------------- //
    // Calendar
    // ------------------------------------------------------ //
    jQuery(function () {
        // page is ready
        jQuery('#calendar').fullCalendar({
            eventLimit: true, 
            themeSystem: 'bootstrap4',
            businessHours: false,
            defaultView: 'month',
            editable: true,
            header: {
                left: 'title',
                center: 'month,agendaWeek,agendaDay',
                right: 'today prev,next'
            },
            dayClick: function () {
                jQuery('#modal-view-event-add').modal();
                selectedDate = new Date($(this).attr('data-date'))
                var picker = $('.datetimepicker').data('datepicker');
                picker.clear()
                picker.selectDate(selectedDate)

            },
            eventClick: function (event, jsEvent, view) {
                jQuery('.event-icon').html("<i class='fa fa-" + event.icon + "'></i>");
                jQuery('.event-title').html(event.title);
                jQuery('.event-body').html(event.description);
                jQuery('.eventUrl').attr('href', event.url);
                jQuery('#modal-view-event').modal();
            },
            eventDrop: function (event, delta, revertFunc) {
                updateEventToGoogle(event)
                // revertFunc()
            },
            eventResize: function (event, delta, revertFunc) {
                updateEventToGoogle(event)
            },
            viewRender: function (event, element) {
                clearEvent();
                // addEventToCalendar();
                var date = event.dateProfile.date
                console.log(date)
                eel.getEventSourcesGoogle(date.year(),date.month()+1)
            }
        })
    });



})(jQuery);


eel.expose(addEventToCalendar)
function addEventToCalendar(events) {
    var calendar = $('#calendar').fullCalendar();
    // console.log("addEventToCalendar is running");
    calendar.data('fullCalendar').addEventSource(events)
    moreCell = $('.fc-more-cell')
    if (moreCell[0])
        moreCell.click(function () {
            $('.fc-more-popover').css('background', '#eee')
        })

}

$('#fuck').click(function () {
    addEventToCalendar()
})

$('#savechange').click(function () {
    var calendar = $('#calendar').fullCalendar();
    console.log(calendar.data('fullCalendar').getEventSources())
});

// $(".fc-next-button, .fc-prev-button, .fc-today-button").click(function () {
$("#clear").click(function () {
    calendar = $('#calendar').fullCalendar().data('fullCalendar');
    calendar.reinitView()
    console.log(calendar);
})




function clearEvent() {
    calendar = $('#calendar').fullCalendar().data('fullCalendar');
    calendar = calendar.eventManager.removeAllSources()
}


function updateEventToGoogle(event) {
    console.log('updatting');
    console.log(event);
}