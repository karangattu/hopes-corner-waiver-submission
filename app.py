from shiny import App, reactive, render, ui
import pandas as pd
from shinyswatch import theme
import base64
import os
import requests
import json
import pytz
from faicons import icon_svg

from dotenv import load_dotenv

_ = load_dotenv()


def get_pacific_time():
    """Get current time in Pacific timezone"""
    pacific_tz = pytz.timezone("US/Pacific")
    return pd.Timestamp.now(tz=pacific_tz)


def get_pacific_date():
    """Get current date in Pacific timezone"""
    return get_pacific_time().date()


waiver_en = """
## SHOWER and LAUNDRY PROGRAM RELEASE FROM LIABILITY

I agree that I, my successors, assignees, heirs, insurers, agents, guardians and legal representatives waive and release any rights, actions, or causes of action against Hope's Corner, Inc., its officers, directors and employees, and any of Hope's Corner, Inc. volunteers or recipients of Hope's Corner services (collectively, the "Released Parties") for injury, death, loss of use, damages arising out of or resulting from the acts or omissions of acts of any person or entity or my activities as a shower program and/or laundry program participant. This includes, without limitation, negligence of any of the Released Parties, whether active or passive, sole or cooperative, or other negligence, however caused, arising from or relating to Hope's Corner or my participation with Hope's Corner in any way. I understand that Hope's Corner would not allow me to participate as a shower program and/or laundry program client without my agreeing to this waiver and release and the other terms of this agreement.

I release and forever discharge the Released Parties from any claim whatsoever arising, or that may arise, on account of any first aid, treatment, or medical service, including the lack of such or timing of such, rendered in connection with my participation as a shower program client.

I acknowledge that an inherent risk of exposure to the disease COVID-19 and any other communicable or infectious disease, exists in any public place where people are present. No precautions can eliminate the risk of exposure to communicable or infectious diseases, and the risk of exposure applies to everyone. I acknowledge that the risk of exposure includes the risk that I will expose others that I later encounter, even if I am not experiencing or displaying any symptoms of illness myself. By visiting and/or participating in Hope's Corner's in-person services I agree to voluntarily assume any and all risks in any way related to exposure to COVID-19 and any other communicable or infectious disease, including illness, injury, or death of myself or others, and including without limitation, all risks based on the sole, joint, active or passive negligence of any of the Released Parties, named below. I acknowledge that my participation is entirely voluntary.

If any provision in this Agreement is held invalid or unenforceable, the other provisions will remain enforceable, and the invalid or unenforceable provision will be considered modified so that it is valid and enforceable to the maximum extent permitted by law. I understand that this agreement will survive the termination of my participation and the assignment of this Agreement by Hope's Corner to any successor or other assignee and will be binding upon my heirs and legal representatives.

**I (PARTICIPANT) FOR MYSELF AND ANY MINOR CHILDREN FOR WHICH I AM PARENT, LEGAL GUARDIAN OR OTHERWISE RESPONSIBLE, HAVE READ THIS ENTIRE RELEASE, I FULLY UNDERSTAND IT, AND I AGREE TO BE LEGALLY BOUND BY IT.**

## ELECTRONIC SIGNATURE AGREEMENT

By entering my full name and initials in the form below, I agree that my electronic signature is the legally binding equivalent of my handwritten signature. I will not contest the legally binding nature, validity, or enforceability of this agreement based on the fact that I signed it electronically. I understand that I have the right to request a paper copy of this waiver by contacting Hope's Corner directly, and that signing electronically does not diminish my rights under this agreement.
"""

agreement_en = f"""
## {get_pacific_date().year} PARTICIPANT AGREEMENT

The shower and laundry services are reserved for **<u>unhoused</u>** individuals.

- Guests will make a reservation for a shower and/or laundry appointment during the meal program. Appointment times are available on a first-come, first-serve basis and are available for the current day only. When all appointment times are filled, participants will be offered the opportunity to join the waitlist.
- Participants will complete the Liability Waiver and Participant Agreement before using the program for the first time. An updated agreement and/or waiver may be needed from time-to-time if required by City, State or County requirements. Participants must complete other documentation or health screenings if required by the County Health Department.
- Participants must comply with County Health Guidelines to participate in the program. Participants experiencing any symptoms of illness are not to enter the property.
- Participants will be onsite and ready for their appointment at least 5 minutes before their scheduled time. Late arrival will result in forfeiture of the appointment.
- Hope's Corner is committed to providing an environment free of discrimination, harassment, inappropriate language or behavior. All participants are expected to use polite language, follow instructions without arguing and follow program rules. Any violation will result in consequences up to and including suspension and/or permanent ban from utilizing services at Hope's Corner.
- Shower participants are allowed a maximum of 15 minutes in the shower room. Shower water usage is limited to a maximum of 5 minutes of running water time.
- Leave the shower room clean. Use your towel to wipe down the sink and other wet areas, dry the floor, remove all personal belongings, place trash in the garbage bin. Inform staff when you are done so the room can be checked for cleanliness. Place your used towel and bathmat in the designated laundry bin when done.
- Please do not flush anything but toilet tissue down the toilets.
- Laundry Service is limited to one load per guest, per week. A load of laundry is 2/3 of a Hope's Corner mesh laundry sack.
- To avoid damage to the equipment, be sure to empty all pockets. We cannot wash bulky items (blankets, pillows, sleeping bags, etc.), extremely dirty items, items with loose parts or pieces, metal items, shoes, or other hard materials.
- All laundry is washed in hot water and dried on high heat. All colors are washed together.
- Hope's Corner laundry (aprons, bath towels, kitchen towels, etc.) will be added to participant laundry load when space allows. We will never add items that belong to another participant.
- We will do our best to complete participant laundry on the same day, however this is not guaranteed. If you need your laundry the same day, do not utilize this service.
- Laundry left for more than 1 week will be donated or discarded.
- Absolutely no smoking, vaping, alcohol, drugs, weapons or animals (except certified service animals) are permitted on the premises.
- Please notify a staff or volunteer if you notice anything in need of repair or maintenance while utilizing the program.
- Hope's Corner, Inc, volunteers and staff are not responsible for lost or stolen property.

**I agree to follow the shower and laundry program rules and acknowledge that any violation of the rules will result in suspension and/or exclusion from future use of the showers and/or laundry.**
"""

waiver_es = """
## EXENCIÓN DE RESPONSABILIDAD DEL PROGRAMA DE DUCHAS y LAVANDERÍA

Acepto que yo, mis sucesores, cesionarios, herederos, aseguradores, agentes, tutores y representantes legales renuncio y libero cualquier derecho, acción o causa de acción contra Hope's Corner, Inc., sus funcionarios, directores y empleados, y cualquiera de los voluntarios o beneficiarios de los servicios de Hope's Corner, Inc. (colectivamente, las "Partes Exoneradas") por lesiones, muerte, pérdida de uso, daños que surjan de o resulten de los actos u omisiones de actos de cualquier persona o entidad o mis actividades como participante del programa de duchas y/o lavandería. Esto incluye, sin limitación, la negligencia de cualquiera de las Partes Exoneradas, ya sea activa o pasiva, única o cooperativa, u otra negligencia, cualquiera que sea su causa, que surja de o se relacione con Hope's Corner o mi participación con Hope's Corner de cualquier manera. Entiendo que Hope's Corner no me permitiría participar como cliente del programa de duchas y/o lavandería sin mi aceptación de esta exención y liberación y los demás términos de este acuerdo.

Libero y descargo para siempre a las Partes Exoneradas de cualquier reclamo que surja, o pueda surgir, a causa de cualquier primer auxilio, tratamiento o servicio médico, incluida la falta de este o el momento de este, prestado en conexión con mi participación como cliente del programa de duchas.

Reconozco que existe un riesgo inherente de exposición a la enfermedad COVID-19 y cualquier otra enfermedad comunicable o infecciosa en cualquier lugar público donde haya personas presentes. Ninguna precaución puede eliminar el riesgo de exposición a enfermedades comunicables o infecciosas, y el riesgo de exposición se aplica a todos. Reconozco que el riesgo de exposición incluye el riesgo de que exponga a otros que encuentre más tarde, incluso si no estoy experimentando o mostrando ningún síntoma de enfermedad. Al visitar y/o participar en los servicios presenciales de Hope's Corner, acepto asumir voluntariamente todos y cada uno de los riesgos relacionados de cualquier manera con la exposición a COVID-19 y cualquier otra enfermedad comunicable o infecciosa, incluyendo enfermedad, lesión o muerte mía o de otros, e incluyendo sin limitación, todos los riesgos basados en la negligencia única, conjunta, activa o pasiva de cualquiera de las Partes Exoneradas, nombradas a continuación. Reconozco que mi participación es enteramente voluntaria.

Si alguna disposición de este Acuerdo se considera inválida o inaplicable, las demás disposiciones seguirán siendo aplicables, y la disposición inválida o inaplicable se considerará modificada para que sea válida y aplicable en la máxima medida permitida por la ley. Entiendo que este acuerdo sobrevivirá a la terminación de mi participación y la cesión de este Acuerdo por parte de Hope's Corner a cualquier sucesor u otro cesionario y será vinculante para mis herederos y representantes legales.

**YO (PARTICIPANTE) POR MÍ MISMO Y POR CUALQUIER HIJO MENOR DEL CUAL SOY PADRE/MADRE, TUTOR LEGAL U OTRO RESPONSABLE, HE LEÍDO ESTA EXENCIÓN COMPLETA, LA ENTIENDO TOTALMENTE Y ACEPTO ESTAR LEGALMENTE OBLIGADO POR ELLA.**

## ACUERDO DE FIRMA ELECTRÓNICA

Al ingresar mi nombre completo e iniciales en el formulario a continuación, acepto que mi firma electrónica es legalmente equivalente a mi firma manuscrita. No impugnaré la naturaleza legalmente vinculante, validez o aplicabilidad de este acuerdo basándome en el hecho de que lo firmé electrónicamente. Entiendo que tengo derecho a solicitar una copia en papel de esta exención contactando directamente a Hope's Corner, y que firmar electrónicamente no disminuye mis derechos bajo este acuerdo.
"""

agreement_es = f"""
## ACUERDO DE PARTICIPANTE {get_pacific_date().year}

Los servicios de ducha y lavandería están reservados para personas **<u>sin hogar</u>**.

- Los invitados harán una reserva para una cita de ducha y/o lavandería durante el programa de comidas. Los horarios de citas están disponibles por orden de llegada y están disponibles solo para el día actual. Cuando se llenan todos los horarios de citas, se ofrecerá a los participantes la oportunidad de unirse a la lista de espera.
- Los participantes completarán la Exención de Responsabilidad y el Acuerdo de Participante antes de usar el programa por primera vez. Es posible que se necesite un acuerdo y/o exención actualizado de vez en cuando si lo requieren los requisitos de la Ciudad, el Estado o el Condado. Los participantes deben completar otra documentación o exámenes de salud si lo requiere el Departamento de Salud del Condado.
- Los participantes deben cumplir con las Directrices de Salud del Condado para participar en el programa. Los participantes que experimenten cualquier síntoma de enfermedad no deben ingresar a la propiedad.
- Los participantes estarán en el lugar y listos para su cita al menos 5 minutos antes de la hora programada. La llegada tardía resultará en la pérdida de la cita.
- Hope's Corner se compromete a proporcionar un ambiente libre de discriminación, acoso, lenguaje o comportamiento inapropiado. Se espera que todos los participantes usen un lenguaje educado, sigan instrucciones sin discutir y sigan las reglas del programa. Cualquier violación resultará en consecuencias que pueden incluir la suspensión y/o prohibición permanente de utilizar los servicios en Hope's Corner.
- Los participantes de la ducha tienen un máximo de 15 minutos en la sala de duchas. El uso del agua de la ducha está limitado a un máximo de 5 minutos de tiempo de agua corriente.
- Deje la sala de duchas limpia. Use su toalla para limpiar el lavabo y otras áreas mojadas, seque el piso, retire todas sus pertenencias personales, coloque la basura en el bote de basura. Informe al personal cuando haya terminado para que se pueda verificar la limpieza de la habitación. Coloque su toalla y alfombra de baño usadas en el contenedor de ropa designado cuando termine.
- Por favor, no tire nada más que papel higiénico por los inodoros.
- El servicio de lavandería está limitado a una carga por invitado, por semana. Una carga de ropa es 2/3 de una bolsa de lavandería de malla de Hope's Corner.
- Para evitar daños al equipo, asegúrese de vaciar todos los bolsillos. No podemos lavar artículos voluminosos (mantas, almohadas, sacos de dormir, etc.), artículos extremadamente sucios, artículos con piezas sueltas, artículos metálicos, zapatos u otros materiales duros.
- Toda la ropa se lava con agua caliente y se seca con calor alto. Todos los colores se lavan juntos.
- La ropa de Hope's Corner (delantales, toallas de baño, toallas de cocina, etc.) se agregará a la carga de lavandería del participante cuando el espacio lo permita. Nunca agregaremos artículos que pertenezcan a otro participante.
- Haremos todo lo posible para completar la lavandería del participante el mismo día, sin embargo, esto no está garantizado. Si necesita su lavandería el mismo día, no utilice este servicio.
- La ropa dejada por más de 1 semana será donada o descartada.
- Absolutamente no se permite fumar, vapear, alcohol, drogas, armas o animales (excepto animales de servicio certificados) en las instalaciones.
- Por favor notifique a un miembro del personal o voluntario si nota algo que necesite reparación o mantenimiento mientras utiliza el programa.
- Hope's Corner, Inc, los voluntarios y el personal no son responsables de la propiedad perdida o robada.

**Acepto seguir las reglas del programa de duchas y lavandería y reconozco que cualquier violación de las reglas resultará en la suspensión y/o exclusión del uso futuro de las duchas y/o lavandería.**
"""

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.style(
            """
            .logo {
                max-width: 250px;
                height: auto;
                display: block;
                margin: 0 auto 20px auto;
            }
            
            .waiver-accordion-container {
                margin-bottom: 30px;
            }
            .accordion-instructions {
                background: linear-gradient(135deg, #e3f2fd, #f3e5f5);
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 15px;
                font-weight: 500;
                border-left: 4px solid #2196f3;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .waiver-content, .agreement-content {
                max-height: 400px;
                overflow-y: auto;
                padding: 15px;
                background-color: #fafafa;
                border-radius: 5px;
                line-height: 1.6;
            }
            
            /* Progress Steps */
            .form-progress {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
            }
            .progress-steps {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 15px;
            }
            .step {
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: 500;
            }
            .step-completed {
                background: #4caf50;
                color: white;
            }
            .step-active {
                background: #2196f3;
                color: white;
            }
            .step-pending {
                background: #e0e0e0;
                color: #666;
            }
            .step-arrow {
                color: #666;
                font-weight: bold;
            }
            
            .form-section {
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            .required-field label::after {
                content: " *";
                color: #f44336;
                font-weight: bold;
            }
            .optional-field {
                opacity: 0.9;
            }
            .field-help {
                font-size: 13px;
                color: #666;
                margin-top: 5px;
                font-style: italic;
            }
            
            .acknowledgment-section {
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
            }
            .acknowledgment-checkboxes {
                margin: 20px 0;
            }
            .acknowledgment-checkboxes .form-group {
                margin-bottom: 15px;
                padding: 12px;
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                background: #f9f9f9;
                transition: all 0.3s ease;
            }
            .acknowledgment-checkboxes .form-group:hover {
                border-color: #2196f3;
                background: #f5f5f5;
            }
            .acknowledgment-checkboxes input[type="checkbox"]:checked + .checkbox-label {
                color: #28a745;
                font-weight: 500;
            }
            .checkbox-label {
                margin-left: 8px;
                line-height: 1.4;
                cursor: pointer;
            }
            .checkbox-label .spanish-text {
                color: #666;
                font-style: italic;
            }
            .required-asterisk {
                color: #f44336;
                font-weight: bold;
            }
            .acknowledgment-note {
                background: #fff3cd;
                border: 1px solid #ffeaa7;
                border-radius: 6px;
                padding: 10px 15px;
                margin-top: 15px;
            }
            .acknowledgment-note p {
                margin: 0;
                font-size: 14px;
                color: #856404;
                font-weight: 500;
            }
            
            .signature-section {
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
            }
            .signature-instructions {
                margin-bottom: 15px;
            }
            .signature-tips {
                font-size: 13px;
                color: #666;
                font-style: italic;
                margin-top: 8px;
            }
            .signature-canvas {
                border: 2px solid #ddd;
                border-radius: 8px;
                cursor: crosshair;
                margin: 15px 0;
                /* Prevent scrolling/zooming gestures from interfering with drawing */
                touch-action: none;
                -ms-touch-action: none;
                transition: border-color 0.3s ease;
            }
            .signature-canvas:hover {
                border-color: #2196f3;
            }
            .signature-controls {
                text-align: center;
                margin-top: 15px;
            }
            
            /* Submit Section */
            .submit-section {
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                text-align: center;
            }
            .submit-checklist {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                border-left: 4px solid #28a745;
            }
            .submit-checklist ul {
                text-align: left;
                margin: 10px 0;
                padding-left: 20px;
            }
            .submit-checklist li {
                margin: 5px 0;
                color: #28a745;
                font-weight: 500;
            }
            .btn-large {
                padding: 15px 30px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                min-width: 250px;
            }
            .submit-btn {
                background: linear-gradient(135deg, #28a745, #20c997);
                border: none;
                transition: all 0.3s ease;
            }
            .submit-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(40, 167, 69, 0.3);
            }
            .submit-btn:disabled {
                opacity: 0.6;
                transform: none;
                cursor: not-allowed;
            }
            
            .progress-modal {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.7);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
            }
            .progress-modal.show {
                opacity: 1;
                visibility: visible;
            }
            .progress-modal-content {
                background: white;
                padding: 40px;
                border-radius: 15px;
                text-align: center;
                max-width: 400px;
                width: 90%;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                transform: scale(0.9);
                transition: transform 0.3s ease;
            }
            .progress-modal.show .progress-modal-content {
                transform: scale(1);
            }
            .progress-spinner {
                width: 50px;
                height: 50px;
                border: 4px solid #f3f3f3;
                border-top: 4px solid #2196f3;
                border-radius: 50%;
                animation: spin 1s linear infinite;
                margin: 0 auto 20px;
            }
            .progress-steps-indicator {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 20px 0;
                font-size: 12px;
            }
            .progress-step-indicator {
                flex: 1;
                text-align: center;
                opacity: 0.5;
                transition: opacity 0.3s ease;
            }
            .progress-step-indicator.active {
                opacity: 1;
                color: #2196f3;
                font-weight: bold;
            }
            .progress-step-indicator.completed {
                opacity: 1;
                color: #28a745;
                font-weight: bold;
            }
            .progress-line {
                height: 2px;
                background: #e0e0e0;
                flex: 2;
                margin: 0 10px;
                position: relative;
                overflow: hidden;
            }
            .progress-line.active {
                background: #2196f3;
            }
            .progress-line.completed {
                background: #28a745;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .lang-buttons {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 15px;
                flex-wrap: wrap;
            }
            .lang-buttons p {
                margin: 0;
                font-weight: 500;
                color: #333;
            }
            
            /* Mobile Responsiveness */
            @media (max-width: 768px) {
                .progress-steps {
                    flex-direction: column;
                    text-align: center;
                }
                .step-arrow {
                    transform: rotate(90deg);
                }
                .signature-canvas {
                    max-width: 100%;
                    width: 100%;
                }
                .btn-large {
                    min-width: 100%;
                    padding: 12px 20px;
                }
            }
            
            /* Legacy styles for backwards compatibility */
            .waiver-box {
                border: 1px solid #ddd;
                padding: 15px;
                margin-bottom: 20px;
                max-height: 300px;
                overflow-y: auto;
                background-color: #f9f9f9;
            }
            .clear-signature-btn {
                margin-top: 10px;
            }
            """
        ),
        ui.tags.script(
            """
        $(document).on('shiny:connected', function() {
            // Auto-capitalize initials as the user types
            $('#initials').on('input', function() {
                var input = $(this);
                var start = input[0].selectionStart;
                var end = input[0].selectionEnd;
                input.val(input.val().toUpperCase());
                input[0].setSelectionRange(start, end);
            });
            
            $('#initials').attr('autocapitalize', 'characters');
            
            // Signature pad functionality
            var canvas = document.getElementById('signature-canvas');
            var ctx = canvas.getContext('2d');
            var drawing = false;
            var signatureData = '';
            // Improve line quality
            ctx.lineWidth = 2;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
            
            canvas.width = 600;
            canvas.height = 200;
            
            function clearCanvas() {
                ctx.fillStyle = 'white';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = 'black';
                signatureData = '';
                Shiny.setInputValue('signature_data', '');
                Shiny.setInputValue('signature_drawn', false);
            }
            
            clearCanvas();
            
            function toCanvasXY(clientX, clientY) {
                var rect = canvas.getBoundingClientRect();
                var scaleX = canvas.width / rect.width;
                var scaleY = canvas.height / rect.height;
                return {
                    x: (clientX - rect.left) * scaleX,
                    y: (clientY - rect.top) * scaleY
                };
            }
            
            canvas.addEventListener('mousedown', function(e) {
                drawing = true;
                var p = toCanvasXY(e.clientX, e.clientY);
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
            });
            
            canvas.addEventListener('mousemove', function(e) {
                if (!drawing) return;
                var p = toCanvasXY(e.clientX, e.clientY);
                ctx.lineTo(p.x, p.y);
                ctx.stroke();
            });
            
            ['mouseup','mouseleave'].forEach(function(evt){
                canvas.addEventListener(evt, function() {
                    if (!drawing) return;
                    drawing = false;
                    signatureData = canvas.toDataURL();
                    Shiny.setInputValue('signature_data', signatureData);
                    Shiny.setInputValue('signature_drawn', true);
                });
            });
            
            canvas.addEventListener('touchstart', function(e) {
                e.preventDefault();
                var t = e.touches[0] || e.changedTouches[0];
                if (!t) return;
                drawing = true;
                var p = toCanvasXY(t.clientX, t.clientY);
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
            }, { passive: false });
            
            canvas.addEventListener('touchmove', function(e) {
                e.preventDefault();
                if (!drawing) return;
                var t = e.touches[0] || e.changedTouches[0];
                if (!t) return;
                var p = toCanvasXY(t.clientX, t.clientY);
                ctx.lineTo(p.x, p.y);
                ctx.stroke();
            }, { passive: false });
            
            canvas.addEventListener('touchend', function(e) {
                e.preventDefault();
                if (!drawing) return;
                drawing = false;
                signatureData = canvas.toDataURL();
                Shiny.setInputValue('signature_data', signatureData);
                Shiny.setInputValue('signature_drawn', true);
            }, { passive: false });
            
            canvas.addEventListener('touchcancel', function(e) {
                e.preventDefault();
                drawing = false;
            }, { passive: false });
            
            $(document).on('click', '#clear_signature', function(e) {
                e.preventDefault();
                clearCanvas();
            });
            
            function capturePageScreenshot() {
                return new Promise((resolve) => {
                    // Scroll to top first
                    window.scrollTo(0, 0);
                    
                    // Get full dimensions
                    const fullHeight = Math.max(
                        document.body.scrollHeight,
                        document.body.offsetHeight,
                        document.documentElement.clientHeight,
                        document.documentElement.scrollHeight,
                        document.documentElement.offsetHeight
                    );
                    const fullWidth = Math.max(
                        document.body.scrollWidth,
                        document.body.offsetWidth,
                        document.documentElement.clientWidth,
                        document.documentElement.scrollWidth,
                        document.documentElement.offsetWidth
                    );
                    
                    // Create an absolute positioned div that covers the entire page
                    const containerDiv = document.createElement('div');
                    containerDiv.style.position = 'absolute';
                    containerDiv.style.top = '0';
                    containerDiv.style.left = '0';
                    containerDiv.style.width = fullWidth + 'px';
                    containerDiv.style.height = fullHeight + 'px';
                    containerDiv.style.zIndex = '-1';
                    document.body.appendChild(containerDiv);
                    
                    html2canvas(document.body, {
                        useCORS: true,
                        allowTaint: true,
                        backgroundColor: '#ffffff',
                        scale: 1.5,
                        logging: false,
                        width: fullWidth,
                        height: fullHeight,
                        windowWidth: fullWidth,
                        windowHeight: fullHeight,
                        scrollX: 0,
                        scrollY: 0,
                        x: 0,
                        y: 0,
                        onclone: function(clonedDoc) {
                            const clonedBody = clonedDoc.body;
                            if (clonedBody) {
                                clonedBody.style.overflow = 'visible';
                                clonedBody.style.height = fullHeight + 'px';
                                clonedBody.style.width = fullWidth + 'px';
                            }
                        }
                    }).then(canvas => {
                        // Clean up the container div
                        document.body.removeChild(containerDiv);
                        const screenshot = canvas.toDataURL('image/png');
                        resolve(screenshot);
                    }).catch(error => {
                        // Clean up the container div on error
                        if (document.body.contains(containerDiv)) {
                            document.body.removeChild(containerDiv);
                        }
                        console.error('Screenshot capture failed:', error);
                        resolve(null);
                    });
                });
            }
            
            window.capturePageScreenshot = capturePageScreenshot;
            
            window.clearSignature = clearCanvas;
            
            function updateProgressSteps() {
                const fullName = $('#full_name').val().trim();
                const initials = $('#initials').val().trim();
                const waiverAcknowledged = $('#waiver_read_acknowledged').prop('checked');
                const agreementAcknowledged = $('#agreement_read_acknowledged').prop('checked');
                const hasSignature = signatureData && signatureData.length > 0;
                
                const step2 = $('.progress-steps .step:nth-child(3)');
                if (fullName && initials && waiverAcknowledged && agreementAcknowledged) {
                    step2.removeClass('step-pending step-active').addClass('step-completed');
                    // Update step 3 (Sign & Submit)
                    const step3 = $('.progress-steps .step:nth-child(5)');
                    if (hasSignature) {
                        step3.removeClass('step-pending').addClass('step-active');
                    } else {
                        step3.removeClass('step-completed step-active').addClass('step-active');
                    }
                } else {
                    step2.removeClass('step-completed step-pending').addClass('step-active');
                    const step3 = $('.progress-steps .step:nth-child(5)');
                    step3.removeClass('step-completed step-active').addClass('step-pending');
                }
            }
            
            $('#full_name, #initials, #waiver_read_acknowledged, #agreement_read_acknowledged').on('input change', updateProgressSteps);
            
            const originalSignatureHandler = function() {
                setTimeout(updateProgressSteps, 100); // Small delay to ensure signature data is updated
            };
            
            const originalMouseUp = canvas.onmouseup;
            const originalTouchEnd = canvas.ontouchend;
        });
        
        let progressModal = null;
        let currentProgressStep = 0;
        const progressSteps = [
            { name: 'Capturing', text: 'Capturing form data...', textEs: 'Capturando datos del formulario...' },
            { name: 'Processing', text: 'Processing submission...', textEs: 'Procesando envío...' },
            { name: 'Saving', text: 'Saving to database...', textEs: 'Guardando en base de datos...' },
            { name: 'Complete', text: 'Almost done...', textEs: 'Casi terminado...' }
        ];
        
        function createProgressModal() {
            const modal = $(`
                <div class="progress-modal" id="progressModal">
                    <div class="progress-modal-content">
                        <div class="progress-spinner"></div>
                        <h4 id="progressTitle">Processing Your Submission</h4>
                        <p id="progressSubtitle">Please wait while we process your waiver...</p>
                        <div class="progress-steps-indicator">
                            <div class="progress-step-indicator active" id="step0">
                                <i class="fas fa-camera"></i><br>Capture
                            </div>
                            <div class="progress-line" id="line0"></div>
                            <div class="progress-step-indicator" id="step1">
                                <i class="fas fa-cog"></i><br>Process
                            </div>
                            <div class="progress-line" id="line1"></div>
                            <div class="progress-step-indicator" id="step2">
                                <i class="fas fa-database"></i><br>Save
                            </div>
                            <div class="progress-line" id="line2"></div>
                            <div class="progress-step-indicator" id="step3">
                                <i class="fas fa-check"></i><br>Done
                            </div>
                        </div>
                        <p style="font-size: 12px; color: #666; margin-top: 15px;">
                            <i class="fas fa-info-circle"></i> This may take a few seconds...
                        </p>
                    </div>
                </div>
            `);
            $('body').append(modal);
            return modal;
        }
        
        function showProgressModal() {
            if (!progressModal) {
                progressModal = createProgressModal();
            }
            currentProgressStep = 0;
            updateProgressStep(0);
            progressModal.addClass('show');
            
            // Disable the submit button
            $('#submit').prop('disabled', true);
        }
        
        function hideProgressModal() {
            if (progressModal) {
                progressModal.removeClass('show');
                setTimeout(() => {
                    progressModal.remove();
                    progressModal = null;
                }, 300);
            }
            // Re-enable the submit button
            $('#submit').prop('disabled', false);
        }
        
        function updateProgressStep(stepIndex) {
            currentProgressStep = stepIndex;
            const step = progressSteps[stepIndex];
            const isSpanish = $('input[name="language"]:checked').val() === 'es';
            
            $('#progressSubtitle').text(isSpanish ? step.textEs : step.text);
            
            for (let i = 0; i <= stepIndex; i++) {
                $(`#step${i}`).removeClass('active').addClass('completed');
                if (i < stepIndex) {
                    $(`#line${i}`).removeClass('active').addClass('completed');
                }
            }
            
            if (stepIndex < progressSteps.length - 1) {
                $(`#step${stepIndex + 1}`).addClass('active');
                $(`#line${stepIndex}`).addClass('active');
            }
        }
        
        function nextProgressStep() {
            if (currentProgressStep < progressSteps.length - 1) {
                updateProgressStep(currentProgressStep + 1);
            }
        }
        
        $(document).on('click', '#submit', function(e) {
            const fullName = $('#full_name').val().trim();
            const initials = $('#initials').val().trim();
            const waiverAck = $('#waiver_read_acknowledged').prop('checked');
            const agreementAck = $('#agreement_read_acknowledged').prop('checked');
            
            if (fullName && initials && waiverAck && agreementAck) {
                // Don't show progress modal here - it will be shown after screenshot
                // The server will handle the screenshot capture flow
            }
        });
        
        Shiny.addCustomMessageHandler("clearSignature", function(message) {
            if (window.clearSignature) {
                window.clearSignature();
                // Update progress when signature is cleared
                setTimeout(function() {
                    const step3 = $('.progress-steps .step:nth-child(5)');
                    step3.removeClass('step-completed').addClass('step-pending');
                }, 100);
            }
        });
        
        Shiny.addCustomMessageHandler("hideProgressModal", function(message) {
            hideProgressModal();
        });
        
        Shiny.addCustomMessageHandler("captureScreenshot", function(message) {
            // Take screenshot FIRST, before showing progress modal
            if (window.capturePageScreenshot) {
                window.capturePageScreenshot().then(screenshot => {
                    if (screenshot) {
                        // Now show progress modal after screenshot is captured
                        showProgressModal();
                        setTimeout(() => nextProgressStep(), 800);  // Step 1: Processing
                        setTimeout(() => nextProgressStep(), 1600); // Step 2: Saving  
                        setTimeout(() => nextProgressStep(), 2400); // Step 3: Complete
                        
                        // Send screenshot data to server
                        Shiny.setInputValue('page_screenshot', screenshot);
                    }
                });
            }
        });
        """
        ),
        ui.tags.script(
            src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"
        ),
    ),
    ui.img(
        src="https://images.squarespace-cdn.com/content/5622cd82e4b0501d40689558/2aedb400-89b8-4f93-856f-cd2c7d5385e4/Hopes_Corner_Logo_Green.png?format=1500w&content-type=image%2Fpng",
        class_="logo",
    ),
    ui.div(
        {"class": "lang-buttons"},
        ui.p("Select Language / Seleccionar Idioma:"),
        ui.input_radio_buttons(
            "language",
            "",
            choices={"en": "English", "es": "Español"},
            selected="en",
            inline=True,
        ),
    ),
    ui.div(
        {"class": "waiver-accordion-container"},
        ui.p(
            {"class": "accordion-instructions"},
            [
                icon_svg("clipboard-list"),
                " Please read both sections below carefully before signing / Por favor lea ambas secciones cuidadosamente antes de firmar:",
            ],
        ),
        ui.accordion(
            ui.accordion_panel(
                [
                    icon_svg("file-contract"),
                    " Liability Waiver / Exención de Responsabilidad",
                ],
                ui.div(
                    {"class": "waiver-content"},
                    ui.output_ui("waiver_content"),
                ),
                value="waiver",
            ),
            ui.accordion_panel(
                [
                    icon_svg("handshake"),
                    " Participant Agreement / Acuerdo de Participante",
                ],
                ui.div(
                    {"class": "agreement-content"},
                    ui.output_ui("agreement_content"),
                ),
                value="agreement",
            ),
            id="waiver_accordion",
            open="waiver",
            multiple=False,
        ),
    ),
    ui.div(
        {"class": "form-progress"},
        ui.h4(
            [
                icon_svg("file-pen"),
                " Complete Your Information / Complete Su Información",
            ]
        ),
        ui.div(
            {"class": "progress-steps"},
            ui.span("Step 1: Read Documents", {"class": "step step-completed"}),
            ui.span("→", {"class": "step-arrow"}),
            ui.span("Step 2: Fill Information", {"class": "step step-active"}),
            ui.span("→", {"class": "step-arrow"}),
            ui.span("Step 3: Sign & Submit", {"class": "step step-pending"}),
        ),
    ),
    ui.div(
        {"class": "form-section"},
        ui.div(
            {"class": "form-group required-field"},
            ui.input_text(
                "full_name",
                "Full Name / Nombre Completo *",
                placeholder="Enter your full name / Ingrese su nombre completo",
            ),
        ),
        ui.div(
            {"class": "form-group required-field"},
            ui.input_text(
                "initials",
                "Initials / Iniciales *",
                placeholder="Your initials / Sus iniciales",
            ),
        ),
        ui.div(
            {"class": "form-group optional-field"},
            ui.input_text(
                "minor_names",
                "Minor's Name(s) (if signing for a child) / Nombre(s) del Menor (si firma por un niño)",
                placeholder="Enter minor's name(s) / Ingrese el nombre(s) del menor",
            ),
            ui.p(
                {"class": "field-help"},
                [
                    icon_svg("circle-info"),
                    " Only required if signing for a minor / Solo requerido si firma por un menor",
                ],
            ),
        ),
        ui.div(
            {"class": "form-group"},
            ui.input_date(
                "signature_date",
                "Date / Fecha",
                format="mm-dd-yyyy",
                value=str(get_pacific_date()),
            ),
        ),
    ),
    ui.div(
        {"class": "acknowledgment-section"},
        ui.h4(
            [
                icon_svg("list-check"),
                " Required Acknowledgments / Reconocimientos Requeridos",
            ]
        ),
        ui.div(
            {"class": "acknowledgment-checkboxes"},
            ui.input_checkbox(
                "waiver_read_acknowledged",
                ui.div(
                    {"class": "checkbox-label"},
                    ui.span("I have read and understand the Liability Waiver / "),
                    ui.span(
                        "He leído y entiendo la Exención de Responsabilidad",
                        {"class": "spanish-text"},
                    ),
                    ui.span(" *", {"class": "required-asterisk"}),
                ),
                value=False,
            ),
            ui.input_checkbox(
                "agreement_read_acknowledged",
                ui.div(
                    {"class": "checkbox-label"},
                    ui.span("I have read and agree to the Participant Agreement / "),
                    ui.span(
                        "He leído y acepto el Acuerdo de Participante",
                        {"class": "spanish-text"},
                    ),
                    ui.span(" *", {"class": "required-asterisk"}),
                ),
                value=False,
            ),
        ),
        ui.div(
            {"class": "acknowledgment-note"},
            ui.p(
                [
                    icon_svg("circle-exclamation"),
                    " Both acknowledgments are required to proceed / Ambos reconocimientos son requeridos para proceder",
                ]
            ),
        ),
    ),
    ui.div(
        {"class": "signature-section"},
        ui.h4([icon_svg("signature"), " Digital Signature / Firma Digital"]),
        ui.div(
            {"class": "signature-instructions"},
            ui.p(
                "Please draw your signature in the box below / Por favor dibuje su firma en el cuadro de abajo:"
            ),
            ui.p(
                {"class": "signature-tips"},
                [
                    icon_svg("lightbulb"),
                    " Tips: Use your finger or stylus on mobile, or your mouse on desktop / Consejos: Use su dedo o stylus en móvil, o su ratón en escritorio",
                ],
            ),
        ),
        ui.tags.canvas(
            id="signature-canvas",
            width="600",
            height="200",
            class_="signature-canvas",
            style="border: 2px solid #ddd; border-radius: 5px; cursor: crosshair; display: block; margin: 10px auto; max-width: 100%; background: #fafafa;",
        ),
        ui.div(
            {"class": "signature-controls"},
            ui.input_action_button(
                "clear_signature",
                [icon_svg("trash"), " Clear Signature / Borrar Firma"],
                class_="btn-secondary clear-signature-btn",
            ),
        ),
    ),
    ui.div(
        {"class": "submit-section"},
        ui.div(
            {"class": "submit-checklist"},
            ui.p(
                "Before submitting, please ensure / Antes de enviar, asegúrese de que:"
            ),
            ui.tags.ul(
                ui.tags.li(
                    [
                        icon_svg("check"),
                        " You have read both documents / Ha leído ambos documentos",
                    ]
                ),
                ui.tags.li(
                    [
                        icon_svg("check"),
                        " You have acknowledged reading the Liability Waiver / Ha reconocido leer la Exención de Responsabilidad",
                    ]
                ),
                ui.tags.li(
                    [
                        icon_svg("check"),
                        " You have acknowledged the Participant Agreement / Ha reconocido el Acuerdo de Participante",
                    ]
                ),
                ui.tags.li(
                    [
                        icon_svg("check"),
                        " All required fields are filled / Todos los campos requeridos están llenos",
                    ]
                ),
                ui.tags.li(
                    [
                        icon_svg("check"),
                        " You have provided your signature / Ha proporcionado su firma",
                    ]
                ),
            ),
        ),
        ui.input_action_button(
            "submit",
            [icon_svg("pen-nib"), " Sign & Submit Waiver / Firmar y Enviar Exención"],
            class_="btn-primary btn-large submit-btn",
        ),
    ),
    theme=theme.minty,
)


def save_waiver_screenshot_to_sharepoint(full_name, screenshot_data):
    """Save the waiver screenshot to SharePoint in a default Screenshots folder"""
    try:
        if not screenshot_data or not screenshot_data.startswith("data:image"):
            print("No valid screenshot data provided")
            return None

        header, data = screenshot_data.split(",", 1)
        image_bytes = base64.b64decode(data)

        current_date = get_pacific_time().strftime("%Y-%m-%d")
        sanitized_name = full_name.replace(" ", "_").replace("/", "_")
        filename = f"{sanitized_name}_{current_date}.png"

        access_token = get_access_token()
        if not access_token:
            print("Failed to get access token for screenshot upload")
            return None

        site_id = get_site_id()
        if not site_id:
            print("Failed to get site ID for screenshot upload")
            return None

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/octet-stream",
        }

        screenshots_folder_path = "/Screenshots"
        create_folder_url = (
            f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root/children"
        )
        folder_data = {
            "name": "Screenshots",
            "folder": {},
            "@microsoft.graph.conflictBehavior": "ignore",
        }

        folder_headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        try:
            folder_response = requests.post(
                create_folder_url, headers=folder_headers, json=folder_data
            )
        except Exception as folder_err:
            print(f"Error creating Screenshots folder: {folder_err}")

        upload_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:{screenshots_folder_path}/{filename}:/content"

        response = requests.put(upload_url, headers=headers, data=image_bytes)

        if response.status_code in [200, 201]:
            file_info = response.json()
            file_path = f"{screenshots_folder_path}/{filename}"
            print(f"Screenshot uploaded successfully to SharePoint: {file_path}")
            return file_path
        else:
            print(
                f"Failed to upload screenshot to SharePoint. Status: {response.status_code}"
            )
            print(f"Response: {response.text}")
            return None

    except Exception as e:
        print(f"Error uploading screenshot to SharePoint: {e}")
        return None


SHAREPOINT_CONFIG = {
    "tenant_id": os.getenv("AZURE_TENANT_ID", "YOUR_TENANT_ID"),
    "client_id": os.getenv("AZURE_CLIENT_ID", "YOUR_CLIENT_ID"),
    "client_secret": os.getenv("AZURE_CLIENT_SECRET", "YOUR_CLIENT_SECRET"),
    "site_url": os.getenv(
        "SHAREPOINT_SITE_URL", "https://yourtenant.sharepoint.com/sites/yoursite"
    ),
    "excel_file_path": os.getenv(
        "SHAREPOINT_EXCEL_FILE_PATH", "/Shared Documents/waiver_submissions.xlsx"
    ),
    "worksheet_name": os.getenv("SHAREPOINT_WORKSHEET_NAME", "Sheet1"),
}


def get_access_token():
    """Get access token for Microsoft Graph API using client credentials flow"""
    token_url = f"https://login.microsoftonline.com/{SHAREPOINT_CONFIG['tenant_id']}/oauth2/v2.0/token"

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    data = {
        "client_id": SHAREPOINT_CONFIG["client_id"],
        "client_secret": SHAREPOINT_CONFIG["client_secret"],
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials",
    }

    try:
        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data.get("access_token")
        if not access_token:
            return None
        return access_token
    except requests.exceptions.HTTPError as http_err:
        print(
            f"HTTP error occurred while getting access token: {http_err} - Response: {response.text}"
        )
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred while getting access token: {req_err}")
        return None
    except json.JSONDecodeError as json_err:
        print(
            f"JSON decode error occurred while getting access token: {json_err} - Response: {response.text}"
        )
        return None
    except Exception as e:
        print(f"An unexpected error occurred while getting access token: {e}")
        return None


def get_site_id():
    """Get the SharePoint site ID"""
    access_token = get_access_token()
    if not access_token:
        return None

    site_url_parts = SHAREPOINT_CONFIG["site_url"].replace("https://", "").split("/")
    hostname = site_url_parts[0]
    site_path = "/".join(site_url_parts[1:]) if len(site_url_parts) > 1 else ""

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    try:
        if site_path:
            url = f"https://graph.microsoft.com/v1.0/sites/{hostname}:/{site_path}"
        else:
            url = f"https://graph.microsoft.com/v1.0/sites/{hostname}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        site_data = response.json()
        site_id_value = site_data.get("id")
        if not site_id_value:
            return None
        return site_id_value
    except requests.exceptions.HTTPError as http_err:
        print(
            f"HTTP error occurred while getting site ID: {http_err} - Response: {response.text}"
        )
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred while getting site ID: {req_err}")
        return None
    except json.JSONDecodeError as json_err:
        print(
            f"JSON decode error occurred while getting site ID: {json_err} - Response: {response.text}"
        )
        return None
    except Exception as e:
        print(f"An unexpected error occurred while getting site ID: {e}")
        return None


def get_excel_file_id(site_id):
    """Get the Excel file ID from SharePoint"""
    access_token = get_access_token()
    if not access_token:
        print("DEBUG: get_excel_file_id - Failed to get access token, cannot proceed.")
        return None
    if not site_id:
        print("DEBUG: get_excel_file_id - Site ID is missing, cannot proceed.")
        return None

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    file_path = SHAREPOINT_CONFIG["excel_file_path"].lstrip("/")
    if not file_path:
        print("Error: SharePoint Excel file path is not configured or is empty.")
        return None

    try:
        url = (
            f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{file_path}"
        )
        print(f"DEBUG: Requesting Excel file ID from URL: {url}")
        response = requests.get(url, headers=headers)
        print(f"DEBUG: Get Excel file ID response status: {response.status_code}")
        if response.status_code >= 400:
            print(f"DEBUG: Get Excel file ID response content: {response.text}")
        response.raise_for_status()
        file_data = response.json()
        file_id_value = file_data.get("id")
        if not file_id_value:
            print(f"Error: 'id' not found in Excel file data response: {file_data}")
            return None
        print(f"DEBUG: Excel file ID obtained: {file_id_value}")
        return file_id_value
    except requests.exceptions.HTTPError as http_err:
        print(
            f"HTTP error occurred while getting Excel file ID: {http_err} - Response: {response.text}"
        )
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred while getting Excel file ID: {req_err}")
        return None
    except json.JSONDecodeError as json_err:
        print(
            f"JSON decode error occurred while getting Excel file ID: {json_err} - Response: {response.text}"
        )
        return None
    except Exception as e:
        print(f"An unexpected error occurred while getting Excel file ID: {e}")
        return None


def add_row_to_excel(waiver_data):
    """Add a new row to the Excel file in SharePoint"""
    try:
        access_token = get_access_token()
        if not access_token:
            print("Failed to get access token")
            return False

        site_id = get_site_id()
        if not site_id:
            print("Failed to get site ID")
            return False

        file_id = get_excel_file_id(site_id)
        if not file_id:
            print("Excel file not found, creating it...")
            if create_excel_file_if_not_exists():
                file_id = get_excel_file_id(site_id)
                if not file_id:
                    print("Failed to create or find Excel file after creation")
                    return False
            else:
                print("Failed to create Excel file")
                return False

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        screenshot_path = waiver_data.get("screenshot_path", "")
        screenshot_filename = ""
        if screenshot_path:
            screenshot_filename = screenshot_path.split("/")[-1]

        row_data = {
            "values": [
                [
                    waiver_data.get("submission_date", ""),
                    waiver_data.get("full_name", ""),
                    waiver_data.get("initials", ""),
                    waiver_data.get("minor_names", ""),
                    waiver_data.get("signature_date", ""),
                    waiver_data.get("language", ""),
                    screenshot_filename,
                ]
            ]
        }

        used_range_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{file_id}/workbook/worksheets/{SHAREPOINT_CONFIG['worksheet_name']}/usedRange"
        range_response = requests.get(used_range_url, headers=headers)

        if range_response.status_code == 200:
            range_data = range_response.json()
            row_count = range_data.get("rowCount", 1)
            next_row = row_count + 1
        else:
            next_row = 2

        cell_range = f"A{next_row}:G{next_row}"  # 7 columns (A to G)
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{file_id}/workbook/worksheets/{SHAREPOINT_CONFIG['worksheet_name']}/range(address='{cell_range}')"

        response = requests.patch(url, headers=headers, json=row_data)

        if response.status_code in [200, 201]:
            print("Successfully added row to Excel file")
            return True
        else:
            print(
                f"Failed to add row to Excel file. Status: {response.status_code}, Response: {response.text}"
            )
            return False

    except Exception as e:
        print(f"Error adding row to Excel: {e}")
        return False


def create_excel_file_if_not_exists():
    """Create the Excel file with proper headers if it doesn't exist"""
    try:
        access_token = get_access_token()
        if not access_token:
            return False

        site_id = get_site_id()
        if not site_id:
            return False

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        file_id = get_excel_file_id(site_id)
        if file_id:
            print("Excel file already exists")
            return True

        file_path = SHAREPOINT_CONFIG["excel_file_path"]
        path_parts = file_path.strip("/").split("/")
        file_name = path_parts[-1]
        folder_path = "/".join(path_parts[:-1]) if len(path_parts) > 1 else ""

        print(f"Creating Excel file: {file_name} in folder: {folder_path}")

        current_folder_url = None
        if folder_path:
            folders = folder_path.split("/")
            current_path = ""

            for folder_name in folders:
                if not folder_name:
                    continue

                current_path += "/" + folder_name if current_path else folder_name
                print(
                    f"Checking/creating folder: {folder_name} at path: {current_path}"
                )

                if current_folder_url is None:
                    check_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{current_path}"
                else:
                    check_url = f"{current_folder_url}:/{folder_name}"

                response = requests.get(check_url, headers=headers)

                if response.status_code == 404:
                    if current_folder_url is None:
                        create_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root/children"
                    else:
                        create_url = f"{current_folder_url}/children"

                    folder_data = {
                        "name": folder_name,
                        "folder": {},
                        "@microsoft.graph.conflictBehavior": "ignore",
                    }

                    create_response = requests.post(
                        create_url, headers=headers, json=folder_data
                    )
                    if create_response.status_code not in [200, 201, 409]:
                        print(
                            f"Failed to create folder {folder_name}: {create_response.status_code}"
                        )
                        print(f"Response: {create_response.text}")
                        return False

                    print(f"Created folder: {folder_name}")

                current_folder_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{current_path}"

        if folder_path:
            create_file_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{folder_path}:/children"
        else:
            create_file_url = (
                f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root/children"
            )

        create_file_data = {
            "name": file_name,
            "file": {},
            "@microsoft.graph.conflictBehavior": "rename",
        }

        response = requests.post(
            create_file_url, headers=headers, json=create_file_data
        )

        if response.status_code in [200, 201]:
            file_data = response.json()
            new_file_id = file_data.get("id")

            headers_data = {
                "values": [
                    [
                        "Submission Date",
                        "Full Name",
                        "Initials",
                        "Minor Names",
                        "Signature Date",
                        "Language",
                        "Screenshot File",
                    ]
                ]
            }

            worksheet_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{new_file_id}/workbook/worksheets/{SHAREPOINT_CONFIG['worksheet_name']}/range(address='A1:G1')"
            header_response = requests.patch(
                worksheet_url, headers=headers, json=headers_data
            )

            if header_response.status_code in [200, 201]:
                print("Excel file created successfully with headers")
            else:
                print(
                    f"Excel file created but failed to add headers: {header_response.status_code}"
                )
                print(f"Headers response: {header_response.text}")

            return True
        else:
            print(f"Failed to create Excel file. Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"Error creating Excel file: {e}")
        return False


def list_worksheets_in_file(site_id, file_id):
    """List all worksheets in the Excel file"""
    access_token = get_access_token()
    if not access_token:
        return None

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    try:
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{file_id}/workbook/worksheets"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        worksheets = response.json()
        return [sheet["name"] for sheet in worksheets.get("value", [])]
    except Exception as e:
        print(f"Error listing worksheets: {e}")
        return None


def server(input, output, session):
    screenshot_trigger = reactive.Value(False)

    @output
    @render.ui
    def waiver_content():
        if input.language() == "en":
            return ui.markdown(waiver_en)
        else:
            return ui.markdown(waiver_es)

    @output
    @render.ui
    def agreement_content():
        if input.language() == "en":
            return ui.markdown(agreement_en)
        else:
            return ui.markdown(agreement_es)

    # Add a reactive calculation for capitalized initials
    @reactive.Calc
    def capitalized_initials():
        """Always returns the initials in uppercase"""
        initials = input.initials()
        return initials.upper() if initials else ""

    @reactive.Effect
    @reactive.event(input.submit)
    async def handle_submit():
        if not input.full_name():
            ui.notification_show(
                (
                    "Please enter your full name."
                    if input.language() == "en"
                    else "Por favor ingrese su nombre completo."
                ),
                type="warning",
                duration=5,
            )
            return

        if not input.initials():
            ui.notification_show(
                (
                    "Please enter your initials."
                    if input.language() == "en"
                    else "Por favor ingrese sus iniciales."
                ),
                type="warning",
                duration=5,
            )
            return

        if not input.waiver_read_acknowledged():
            ui.notification_show(
                (
                    "Please confirm that you have read and understand the Liability Waiver."
                    if input.language() == "en"
                    else "Por favor confirme que ha leído y entiende la Exención de Responsabilidad."
                ),
                type="warning",
                duration=5,
            )
            return

        if not input.agreement_read_acknowledged():
            ui.notification_show(
                (
                    "Please confirm that you have read and agree to the Participant Agreement."
                    if input.language() == "en"
                    else "Por favor confirme que ha leído y acepta el Acuerdo de Participante."
                ),
                type="warning",
                duration=5,
            )
            return

        if not input.signature_data() or input.signature_data() == "":
            ui.notification_show(
                (
                    "Please draw your signature in the box before submitting."
                    if input.language() == "en"
                    else "Por favor dibuje su firma en el cuadro antes de enviar."
                ),
                type="warning",
                duration=5,
            )
            return

        try:
            # Trigger screenshot capture BEFORE showing progress modal
            screenshot_trigger.set(True)
            await session.send_custom_message("captureScreenshot", "")
        except Exception as e:
            error_msg_en = f"An error occurred while creating the waiver: {e}"
            error_msg_es = f"Ocurrió un error al crear la exención: {e}"
            ui.notification_show(
                error_msg_en if input.language() == "en" else error_msg_es,
                type="error",
                duration=10,
            )
            print(f"Error creating waiver: {e}")

    @reactive.Effect
    async def save_screenshot():
        if screenshot_trigger.get() and input.page_screenshot():
            screenshot_data = input.page_screenshot()
            screenshot_trigger.set(False)
            if screenshot_data:
                screenshot_path = save_waiver_screenshot_to_sharepoint(
                    input.full_name(), screenshot_data
                )

                if screenshot_path:
                    print(f"Screenshot saved successfully: {screenshot_path}")

                    waiver_data = {
                        "submission_date": get_pacific_time().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                        "full_name": input.full_name(),
                        "initials": input.initials().upper(),
                        "minor_names": input.minor_names() or "",
                        "signature_date": str(input.signature_date()),
                        "language": input.language(),
                        "waiver_acknowledged": (
                            "Yes" if input.waiver_read_acknowledged() else "No"
                        ),
                        "agreement_acknowledged": (
                            "Yes" if input.agreement_read_acknowledged() else "No"
                        ),
                        "screenshot_path": screenshot_path,
                    }

                    sharepoint_success = add_row_to_excel(waiver_data)

                    if sharepoint_success:
                        print("Data successfully saved to Database")
                    else:
                        print("Failed to save data to Database")

                    if input.language() == "en":
                        message = "✓ Thank you! Your waiver has been signed and saved successfully."
                        if sharepoint_success:
                            message += " Data has been saved to Database."
                        else:
                            message += " Note: Could not save to Database."
                    else:
                        message = "✓ ¡Gracias! Su exención ha sido firmada y guardada con éxito."
                        if sharepoint_success:
                            message += " Los datos se han guardado en la base de datos."
                        else:
                            message += " Nota: No se pudo guardar en la base de datos."

                    ui.notification_show(message, type="default", duration=10)

                    await session.send_custom_message("hideProgressModal", "")

                    ui.update_text("full_name", value="")
                    ui.update_text("initials", value="")
                    ui.update_text("minor_names", value="")
                    await session.send_custom_message(
                        "clearSignature", ""
                    )
                else:
                    await session.send_custom_message("hideProgressModal", "")
                    ui.notification_show(
                        "Failed to save screenshot.",
                        type="error",
                        duration=10,
                    )
            else:
                await session.send_custom_message("hideProgressModal", "")
                ui.notification_show(
                    "No screenshot data received.",
                    type="error",
                    duration=10,
                )

    @reactive.Effect
    def _():
        """Ensure initials are always capitalized"""
        current = input.initials()
        if current and current != current.upper():
            ui.update_text("initials", value=current.upper())


app = App(app_ui, server)
