package chatgpt

import (
	"fmt"
	"testing"
)

func TestName(t *testing.T) {
	res, err := NewAIChatGPT().Chat([]*ChatMessage{
		{
			Role:    "user",
			Content: "你好",
		},
	})

	fmt.Println(res)
	fmt.Println(err)
	if err != nil {
		return
	}

}
