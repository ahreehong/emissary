// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: envoy/extensions/filters/network/postgres_proxy/v3alpha/postgres_proxy.proto

package envoy_extensions_filters_network_postgres_proxy_v3alpha

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/golang/protobuf/ptypes"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = ptypes.DynamicAny{}
)

// define the regex for a UUID once up-front
var _postgres_proxy_uuidPattern = regexp.MustCompile("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

// Validate checks the field values on PostgresProxy with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *PostgresProxy) Validate() error {
	if m == nil {
		return nil
	}

	if utf8.RuneCountInString(m.GetStatPrefix()) < 1 {
		return PostgresProxyValidationError{
			field:  "StatPrefix",
			reason: "value length must be at least 1 runes",
		}
	}

	return nil
}

// PostgresProxyValidationError is the validation error returned by
// PostgresProxy.Validate if the designated constraints aren't met.
type PostgresProxyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e PostgresProxyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e PostgresProxyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e PostgresProxyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e PostgresProxyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e PostgresProxyValidationError) ErrorName() string { return "PostgresProxyValidationError" }

// Error satisfies the builtin error interface
func (e PostgresProxyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sPostgresProxy.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = PostgresProxyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = PostgresProxyValidationError{}