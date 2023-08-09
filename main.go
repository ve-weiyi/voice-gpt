package main

import (
	"github.com/gin-gonic/gin"

	"voice-gpt/chatgpt"
)

func main() {
	// 创建一个 Gin 路由引擎
	r := gin.Default()

	// 定义一个 GET 请求的路由，当访问根路径时返回 "Hello, World!"
	r.POST("/api/v1/ai/chat", func(c *gin.Context) {

		var req []*chatgpt.ChatMessage
		err := c.ShouldBindJSON(&req)
		if err != nil {
			c.AbortWithStatusJSON(400, gin.H{})
			return
		}

		data, err := chatgpt.NewAIChatGPT().Chat(req)
		if err != nil {
			c.AbortWithStatusJSON(400, gin.H{})
			return
		}

		c.JSON(200, gin.H{
			"code":    200,
			"message": "Hello, World!",
			"data":    data,
		})
	})

	// 启动服务器并监听在 8080 端口
	r.Run(":9999")
}
