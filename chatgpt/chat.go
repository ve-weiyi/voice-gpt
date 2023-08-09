package chatgpt

import (
	"encoding/json"

	"voice-gpt/utils/https"
	"voice-gpt/utils/jsonconv"
)

type AiMessage struct {
	Role string `json:"role"`
	Msg  []*ChatMessage
}

type ChatGPT interface {
	Chat(request *ChatRequest) (*ChatResponse, error)
}

type AIChatGPT struct {
	ChatGPT
	Url    string `json:"url"`
	ApiKey string `json:"apiKey"`
	Model  string `json:"model"`
}

func NewAIChatGPT() *AIChatGPT {
	return &AIChatGPT{
		Url:    "xx",
		ApiKey: "xx",
		Model:  "gpt-35-turbo",
	}
}

func (s *AIChatGPT) Chat(req []*ChatMessage) (resp *ChatResponse, err error) {
	content := ChatRequest{
		Model:    s.Model,
		Messages: req,
	}

	res, err := https.NewHttpBuilder(s.Url).
		AddHeader("Content-Type", "application/json").
		AddHeader("api-key", s.ApiKey).
		AddBody(jsonconv.ObjectToJson(content)).
		Post()

	if err != nil {
		return nil, err
	}

	resp = &ChatResponse{}
	err = json.Unmarshal([]byte(res), resp)
	if err != nil {
		return nil, err
	}

	return resp, nil
}
