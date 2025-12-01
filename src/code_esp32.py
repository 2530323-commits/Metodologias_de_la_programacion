#include <WiFi.h>
#include <esp_now.h>

// Función que se ejecuta cuando llega un mensaje
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  Serial.print("Datos recibidos: ");
  Serial.println(*incomingData);
}

void setup() {
  Serial.begin(115200);

  // Inicializar Wi-Fi en modo estación
  WiFi.mode(WIFI_STA);

  // Iniciar ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error iniciando ESP-NOW");
    return;
  }

  // Registrar callback de recepción
  esp_now_register_recv_cb(OnDataRecv);

  Serial.println("Receptor listo (ESP-NOW)");
}

void loop() {

}
