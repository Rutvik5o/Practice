<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body id="md" runat="server">
    <form id="form1" runat="server">
    <div>
    
    </div>
    <p>
        Select one of color:</p>
    <p>
        &nbsp;</p>
    <asp:RadioButtonList ID="RadioButtonList1" runat="server" 
        RepeatDirection="Horizontal">
        <asp:ListItem>Red</asp:ListItem>
        <asp:ListItem>Blue</asp:ListItem>
        <asp:ListItem>Yellow</asp:ListItem>
        <asp:ListItem>Grey</asp:ListItem>
        <asp:ListItem>Green</asp:ListItem>
        <asp:ListItem>Purple</asp:ListItem>
        <asp:ListItem>Cyan</asp:ListItem>
        <asp:ListItem>Orange</asp:ListItem>
    </asp:RadioButtonList>
    <br />
    <br />
    <asp:Button ID="Button1" runat="server" Text="Apply color" 
        onclick="Button1_Click" />
    </form>
</body>
</html>
