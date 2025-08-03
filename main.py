#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED_GREEN GPIO_NUM_7
#define LED_YELLOW GPIO_NUM_6
#define LED_RED GPIO_NUM_5

uint32_t led_green_blink_time = 300;
uint32_t led_yellow_blink_time = 1000;
uint32_t led_red_blink_time = 2000;

void led_green_task(void *pvParameter);
void led_yellow_task(void *pvParameter);
void led_red_task(void *pvParameter);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  pinMode(LED_GREEN,OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);

  digitalWrite(LED_GREEN|LED_YELLOW|LED_RED, LOW);

  xTaskCreate( led_green_task, "Led Green Task", 1024, NULL, 3, NULL );
  xTaskCreate( led_yellow_task, "Led Yellow Task", 1024, NULL, 2, NULL );
  xTaskCreate( led_red_task, "Led Red Task", 1024, NULL, 1, NULL );
}

void led_green_task(void *pvParameter)
{
  while(1) {
    vTaskDelay(led_green_blink_time / portTICK_PERIOD_MS);
    digitalWrite(LED_GREEN,!digitalRead(LED_GREEN));
  }
}

void led_yellow_task(void *pvParameter)
{
  while(1) {
    vTaskDelay(led_yellow_blink_time / portTICK_PERIOD_MS);
    digitalWrite(LED_YELLOW,!digitalRead(LED_YELLOW));
  }
}

void led_red_task(void *pvParameter)
{
  while(1) {
    vTaskDelay(led_red_blink_time / portTICK_PERIOD_MS);
    digitalWrite(LED_RED,!digitalRead(LED_RED));
  }
}

void loop() {}
