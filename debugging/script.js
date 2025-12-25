// Debugging Task: Fix the button ID mismatch

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded');
    
    // JavaScript "colorButton" axtarır, amma HTML-də "colorButon" var
    // DÜZƏLİŞ: HTML-dəki ID JavaScript-dəki ilə eyni olmalıdır
    const colorButton = document.getElementById('colorButton');
    
    if (colorButton) {
        console.log('Button found successfully!');
        
        colorButton.addEventListener('click', function() {
            console.log('Button clicked!');
            
            // Rənglər siyahısı
            const colors = [
                '#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0', 
                '#118AB2', '#EF476F', '#073B4C', '#7209B7'
            ];
            
            // Təsadüfi rəng seç
            const randomIndex = Math.floor(Math.random() * colors.length);
            const selectedColor = colors[randomIndex];
            
            // Arxa plan rəngini dəyiş
            document.body.style.backgroundColor = selectedColor;
            
            // Düymə mətnini yenilə
            colorButton.textContent = `Color: ${selectedColor}`;
            
            // Konsola məlumat yaz
            console.log(`Background color changed to: ${selectedColor}`);
        });
    } else {
        console.error('ERROR: Could not find button with ID "colorButton"');
        console.error('Check if HTML button ID matches JavaScript getElementById');
    }
});
