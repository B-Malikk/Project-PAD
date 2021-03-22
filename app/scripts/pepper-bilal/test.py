import time
import threading


class SpeechRecognition:
    session = speech_recognition_service = memory_service = None
    speech_recognition_started = False
    on_speech_recognized_callback = None
    words_list = ['Goedemorgen']

    def __init__(self, session):
        self.session = session
        self.speech_recognition_service = self.session.service("ALSpeechRecognition")
        self.memory_service = self.session.service("ALMemory")

    def set_language(self, language):
        self.speech_recognition_service.setLanguage(language)
        return self

    def process_speech_recognition(self):
            while self.speech_recognition_started:
			        time.sleep(1)

			        recognize = self.memory_service.getData("WordRecognized")

			            if recognize and len(recognize) == 2 and len(recognize[0]) > 0:
				                try:
					            # Remove the event when we get data from it, so we don't get the same data twice.
					                    self.memory_service.removeData("WordRecognized")

					                    word = recognize[0]
					                    probability = recognize[1]

					                    self.stop()
					                    if self.on_speech_recognized_callback:
						                self.on_speech_recognized_callback(word, probability)
				                except RuntimeError:
					            pass

	def start(self):
		self.stop()

		self.speech_recognition_service.setVocabulary(self.words_list, False)
		self.speech_recognition_service.subscribe("Test_ASR")

		self.speech_recognition_started = True

		threading.Thread(target=self.process_speech_recognition).start()

		return self

	def stop(self):
		self.speech_recognition_started = False
		try:
			self.speech_recognition_service.unsubscribe("Test_ASR")
		except:
			print("")
		return self

	def set_on_speech_recognized_callback(self, callback):
		self.on_speech_recognized_callback = callback
		return self

	def set_word_list(self, words):
		self.words_list = words
		return self

