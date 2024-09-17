<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <style type="text/css">
        .style1
        {
            width: 100%;
        }
        .style2
        {
            width: 479px;
        }
        .style3
        {
            width: 479px;
            height: 25px;
        }
        .style4
        {
            height: 25px;
        }
        .style5
        {
            width: 426px;
        }
        .style6
        {
            width: 234px;
        }
        .style7
        {
            width: 290px;
        }
        .style8
        {
            height: 23px;
        }
        .style9
        {
            height: 23px;
            width: 633px;
        }
        .style10
        {
            width: 633px;
        }
        .style11
        {
            height: 25px;
            width: 633px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:Panel ID="Panel1" runat="server" Height="157px">
            <h2>Personal Details:</h2>
            <table class="style1">
                <tr>
                    <td class="style2">
                        Firstname:</td>
                    <td>
                        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style3">
                        Lastname:</td>
                    <td class="style4">
                        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Email:</td>
                    <td>
                        <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Mobile No:</td>
                    <td>
                        <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
                    </td>
                </tr>
            </table>
        </asp:Panel>
    
    </div>
    <asp:Panel ID="Panel2" runat="server" Height="172px">
        <h2>Education Details:</h2>
        <table class="style1">
            <tr>
                <td class="style5">
                    &nbsp;</td>
                <td class="style6">
                    University/Board</td>
                <td class="style7">
                    Passing Year</td>
                <td>
                    Percentage Received</td>
            </tr>
            <tr>
                <td class="style5">
                    SSC</td>
                <td class="style6">
                    <asp:TextBox ID="TextBox5" runat="server" Width="216px"></asp:TextBox>
                </td>
                <td class="style7">
                    <asp:TextBox ID="TextBox9" runat="server"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox13" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style5">
                    HSC</td>
                <td class="style6">
                    <asp:TextBox ID="TextBox6" runat="server" Height="22px" Width="210px"></asp:TextBox>
                </td>
                <td class="style7">
                    <asp:TextBox ID="TextBox10" runat="server"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox14" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style5">
                    Graduate</td>
                <td class="style6">
                    <asp:TextBox ID="TextBox7" runat="server" Width="206px"></asp:TextBox>
                </td>
                <td class="style7">
                    <asp:TextBox ID="TextBox11" runat="server"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox15" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style5">
                    Post Graduate</td>
                <td class="style6">
                    <asp:TextBox ID="TextBox8" runat="server" Width="203px"></asp:TextBox>
                </td>
                <td class="style7">
                    <asp:TextBox ID="TextBox12" runat="server"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox16" runat="server"></asp:TextBox>
                </td>
            </tr>
        </table>
        <br />
        <br />
    </asp:Panel>
    <asp:Panel ID="Panel3" runat="server" Height="159px">
        <h2>Experience Details:</h2>
        <table class="style1">
            <tr>
                <td class="style11">
                    Company Name:</td>
                <td class="style4">
                    <asp:TextBox ID="TextBox20" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style10">
                    From:</td>
                <td>
                    <asp:TextBox ID="TextBox17" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style10">
                    To:</td>
                <td>
                    <asp:TextBox ID="TextBox18" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style9">
                    Post:</td>
                <td class="style8">
                    <asp:TextBox ID="TextBox19" runat="server"></asp:TextBox>
                </td>
            </tr>
        </table>
    </asp:Panel>
    <asp:Panel ID="Panel4" runat="server" Height="63px">
        <asp:Button ID="Button1" runat="server" Text="Submit" onclick="Button1_Click" />
    </asp:Panel>
    </form>
</body>
</html>
