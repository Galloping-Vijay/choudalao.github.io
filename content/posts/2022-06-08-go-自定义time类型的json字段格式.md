---
title: "go 自定义Time类型的JSON字段格式"
date: 2022-06-08T12:07:34+08:00
updated: 2026-02-23T02:39:23+08:00
author: "臭大佬"
categories: [Go]
description: "go 自定义Time类型的JSON字段格式"
cover: "https://www.choudalao.com/uploads/20220608/eE2qa34qLuzs9Tp5lW9tLQxsTKmmgd2ZVeUuKo4V.jpeg"
click: 3244
---

# 问题
在使用



Golang中使用gorm时，通过加入gorm.Model到自己的struct来定义一个model。 Gorm是这样定义Model的：
```go
// UserAuditLog XXXX
type UserAuditLog struct {
	Id        uint32    `json:"id" form:"id"`
	UserId    uint32    `json:"user_id" form:"user_id"`
	Status    uint32    `json:"status" form:"audit_status"`
	Reason    string    `json:"reason" form:"reason"`
	AuditorId uint32    `json:"auditor_id" form:"created_at"`
	CreatedAt time.Time `json:"created_at" form:"created_at"`
}
```
当我们的API在接收到查询请求时返回一个model通过JSON形式返回给客户端，这时类型为time.Time的字段就会默认以RFC3339的格式返回，所有的这类字段的返回值都固定是2006-01-02T15:04 :05.999999999Z07:00这种格式

```go 
const (
    ANSIC       = "Mon Jan _2 15:04:05 2006"
    UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
    RubyDate    = "Mon Jan 02 15:04:05 -0700 2006"
    RFC822      = "02 Jan 06 15:04 MST"
    RFC822Z     = "02 Jan 06 15:04 -0700" // RFC822 with numeric zone
    RFC850      = "Monday, 02-Jan-06 15:04:05 MST"
    RFC1123     = "Mon, 02 Jan 2006 15:04:05 MST"
    RFC1123Z    = "Mon, 02 Jan 2006 15:04:05 -0700" // RFC1123 with numeric zone
    RFC3339     = "2006-01-02T15:04:05Z07:00"
    RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"
    Kitchen     = "3:04PM"
    // Handy time stamps.
    Stamp      = "Jan _2 15:04:05"
    StampMilli = "Jan _2 15:04:05.000"
    StampMicro = "Jan _2 15:04:05.000000"
    StampNano  = "Jan _2 15:04:05.000000000"
)
```

修改方式如下：
 
# 代码
```go
package time2

import (
	"database/sql/driver"
	"fmt"
	"time"
)

// JsonTime 格式化时间格式
type JsonTime struct {
	time.Time
}

// MarshalJSON on JsonTime format Time field with %Y-%m-%d %H:%M:%S
func (t JsonTime) MarshalJSON() ([]byte, error) {
	formatted := fmt.Sprintf("\"%s\"", t.Format("2006-01-02 15:04:05"))
	return []byte(formatted), nil
}

// Value insert timestamp into mysql need this function.
func (t JsonTime) Value() (driver.Value, error) {
	var zeroTime time.Time
	if t.Time.UnixNano() == zeroTime.UnixNano() {
		return nil, nil
	}
	return t.Time, nil
}

// Scan valueof time.Time
func (t *JsonTime) Scan(v interface{}) error {
	value, ok := v.(time.Time)
	if ok {
		*t = JsonTime{Time: value}
		return nil
	}
	return fmt.Errorf("can not convert %v to timestamp", v)
}
```

### 使用
结构体如下：
```go
package entity
import  time2"time2"

// UserAuditLog XXXX
type UserAuditLog struct {
	Id        uint32         `json:"id" form:"id"`
	UserId    uint32         `json:"user_id" form:"user_id"`
	Status    uint32         `json:"status" form:"audit_status"`
	Reason    string         `json:"reason" form:"reason"`
	AuditorId uint32         `json:"auditor_id" form:"created_at"`
	CreatedAt time2.JsonTime `json:"created_at" form:"created_at"`
}
```

赋值
```go
package user
import (
time2 "time2"
	"time"
	)
UserAuditLog.CreatedAt = time2.JsonTime{
	Time: time.Now(),
}
```

参考文章
https://www.axiaoxin.com/article/241/